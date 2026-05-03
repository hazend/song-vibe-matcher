from fastapi import FastAPI, HTTPException
from models import Song, VibeAnalysis, SongLookup
from services import analyze_vibe, get_song_by_name

app = FastAPI(title="Song Vibe Matcher API", version="0.1")

@app.get("/")
async def root():
    return {"message": "Song Vibe Matcher API v0.1 is running"}

'''
Endpoint to analyze song vibes by name
Input: JSON with song_name
Output: JSON with sentiment score, mood, and compound score
'''
@app.post("/analyze", response_model=VibeAnalysis)
async def analyze_song(request: SongLookup):
    song = get_song_by_name(request.song_name)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found in database")
    return analyze_vibe(song)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # Run this file/ server using 'python backend/main.py'
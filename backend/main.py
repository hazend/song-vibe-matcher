from fastapi import FastAPI
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI(title="Song Vibe Matcher API", version="0.1")
analyzer = SentimentIntensityAnalyzer()

class Song(BaseModel):
    artist: str
    title: str
    lyrics: str

class VibeAnalysis(BaseModel):
    artist: str
    title: str
    sentiment_score: float
    mood: str
    compound_score: float

def get_mood(compound: float) -> str:
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

@app.get("/")
async def root():
    return {"message": "Song Vibe Matcher API v0.1 is running"}

@app.post("/analyze", response_model=VibeAnalysis)
async def analyze_song(song: Song):
    # Perform sentiment analysis using VADER
    scores = analyzer.polarity_scores(song.lyrics)
    compound = scores['compound']
    
    return VibeAnalysis(
        artist=song.artist,
        title=song.title,
        sentiment_score=compound,
        mood=get_mood(compound),
        compound_score=compound
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # Run this file/ server using 'python backend/main.py'
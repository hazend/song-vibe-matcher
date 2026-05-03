from pydantic import BaseModel

class Song(BaseModel):
    artist: str
    title: str
    lyrics: str

class SongLookup(BaseModel):
    song_name: str

class VibeAnalysis(BaseModel):
    artist: str
    title: str
    sentiment_score: float
    mood: str
    compound_score: float

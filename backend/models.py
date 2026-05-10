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
    sentiment_score: float          # VADER compound score (-1 to 1)
    compound_score: float           # kept for backward compatibility
    mood: str                       # Positive / Negative / Neutral
    # --- v0.2 enrichments ---
    subjectivity: float = 0.0       # TextBlob (0 = objective, 1 = highly emotional)
    vibe_label: str = ""            # human-readable vibe (e.g. "Euphoric / Dreamy")
    keywords: list[str] = []        # top-5 lyric content words
    image_url: str | None = None    # populated in v0.3 by image_gen

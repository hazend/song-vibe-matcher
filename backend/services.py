import json
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from models import Song, VibeAnalysis

analyzer = SentimentIntensityAnalyzer()

'''
Returns the mood of the song based on the compound score
'''
def get_mood(compound: float) -> str:
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

'''
Performs sentiment analysis using VADER
'''
def analyze_vibe(song: Song) -> VibeAnalysis:
    scores = analyzer.polarity_scores(song.lyrics)
    compound = scores['compound']
    
    return VibeAnalysis(
        artist=song.artist,
        title=song.title,
        sentiment_score=compound,
        mood=get_mood(compound),
        compound_score=compound
    )

'''
Returns song by name from the local json database
'''
def get_song_by_name(song_name: str) -> Song:
    # Get the path to the Songs.json file and load the data
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Songs.json')
    with open(data_path, 'r') as f:
        songs_data = json.load(f)
    
    # Iterate through the songs data to find the song by name
    for item in songs_data:
        if item['song'].lower() == song_name.lower():
            return Song(
                artist=item['artist'],
                title=item['song'],
                lyrics=item['lyrics']
            )
    return None

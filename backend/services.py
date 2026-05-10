import json
import os
from models import Song, VibeAnalysis

# Delegate vibe analysis to the enriched ML module (v0.2).
# Re-exported here so main.py needs no import changes.
from ml.analyzer import analyze_vibe

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

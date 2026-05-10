"""
backend/ml/analyzer.py

Enriched NLP vibe-analysis pipeline for Song Vibe Matcher v0.2.

Pipeline stages:
    1. VADER  — compound score + pos/neg/neu ratios
    2. TextBlob — subjectivity score (0 = objective, 1 = highly emotional)
    3. Keyword extraction — NLTK tokenize + stopword filter → top-5 content words
    4. Vibe label mapping — compound X subjectivity → human-readable label
"""

import sys
import os

# ---------------------------------------------------------------------------
# Allow imports from the parent `backend/` directory when this module is run
# directly or called from main.py with a relative sys.path.
# ---------------------------------------------------------------------------
_BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _BACKEND_DIR not in sys.path:
    sys.path.insert(0, _BACKEND_DIR)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from models import Song, VibeAnalysis

# ---------------------------------------------------------------------------
# Module-level singletons (initialised once on import)
# ---------------------------------------------------------------------------
_vader = SentimentIntensityAnalyzer()
_STOPWORDS: set[str] = set(stopwords.words("english"))

# Punctuation / single-char tokens we never want as keywords
_MIN_KEYWORD_LEN = 3


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _get_mood(compound: float) -> str:
    """Map VADER compound score to a coarse mood label."""
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    return "Neutral"


def _map_vibe_label(compound: float, subjectivity: float) -> str:
    """
    Map (compound, subjectivity) onto a human-readable vibe label.

    Vibe Label Matrix
    -----------------
    compound     | subjectivity | label
    -------------|--------------|------------------
    >= 0.35      | >= 0.5       | Euphoric / Dreamy
    >= 0.35      | <  0.5       | Uplifting / Anthemic
    -0.35 to 0.35| >= 0.5       | Introspective / Melancholic
    -0.35 to 0.35| <  0.5       | Chill / Laid-back
    <= -0.35     | >= 0.5       | Heartbroken / Intense
    <= -0.35     | <  0.5       | Dark / Brooding
    """
    if compound >= 0.35:
        return "Euphoric / Dreamy" if subjectivity >= 0.5 else "Uplifting / Anthemic"
    elif compound <= -0.35:
        return "Heartbroken / Intense" if subjectivity >= 0.5 else "Dark / Brooding"
    else:  # neutral band
        return "Introspective / Melancholic" if subjectivity >= 0.5 else "Chill / Laid-back"


def _extract_keywords(text: str, top_n: int = 5) -> list[str]:
    """
    Return the top-N most-frequent content words from *text*.

    Steps:
        1. Lowercase + NLTK word tokenization
        2. Remove stopwords, non-alpha tokens, and very short tokens
        3. Sort by frequency (descending) and return top_n
    """
    tokens = word_tokenize(text.lower())
    content_words = [
        t for t in tokens
        if t.isalpha()
        and len(t) >= _MIN_KEYWORD_LEN
        and t not in _STOPWORDS
    ]

    # frequency map → sorted by count desc → take top_n unique words
    freq: dict[str, int] = {}
    for word in content_words:
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq, key=lambda w: freq[w], reverse=True)
    return sorted_words[:top_n]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def analyze_vibe(song: Song) -> VibeAnalysis:
    """
    Run the full enriched NLP pipeline on *song* and return a VibeAnalysis.

    Ported and extended from the original services.analyze_vibe() in v0.1.
    """
    lyrics = song.lyrics

    # -- Stage 1: VADER sentiment -------------------------------------------
    vader_scores = _vader.polarity_scores(lyrics)
    compound = vader_scores["compound"]

    # -- Stage 2: TextBlob subjectivity -------------------------------------
    blob = TextBlob(lyrics)
    subjectivity: float = blob.sentiment.subjectivity  # 0.0 – 1.0

    # -- Stage 3: Keyword extraction ----------------------------------------
    keywords = _extract_keywords(lyrics)

    # -- Stage 4: Vibe label ------------------------------------------------
    vibe_label = _map_vibe_label(compound, subjectivity)
    mood = _get_mood(compound)

    return VibeAnalysis(
        artist=song.artist,
        title=song.title,
        sentiment_score=compound,
        subjectivity=round(subjectivity, 4),
        mood=mood,
        vibe_label=vibe_label,
        keywords=keywords,
        compound_score=compound,   # kept for backward compat
        image_url=None,            # populated in v0.3 by image_gen
    )

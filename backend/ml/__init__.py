"""
backend/ml/__init__.py

ML service package for Song Vibe Matcher.
Exposes the primary analysis entry point so callers can simply do:

    from ml import analyze_vibe
"""

from .analyzer import analyze_vibe

__all__ = ["analyze_vibe"]

"""
backend/ml/image_gen.py

GenAI vibe-image generator — STUB for v0.2.

This module keeps the model contract stable so the frontend `image_url`
field is ready the moment a real generator is wired in during v0.3.

Replace the body of `generate_vibe_image` in v0.3 with an actual call to
a GenAI provider (e.g. Google Imagen, OpenAI DALL·E, Stability AI, etc.).
"""


def generate_vibe_image(vibe_label: str, keywords: list[str]) -> str | None:
    """
    Generate (or fetch) a vibe-representative image URL for a song.

    Parameters
    ----------
    vibe_label : str
        Human-readable vibe label produced by `analyzer.py`
        (e.g. "Euphoric / Dreamy", "Dark / Brooding").
    keywords : list[str]
        Top lyric keywords to use as additional prompt context.

    Returns
    -------
    str | None
        URL of the generated image, or ``None`` if generation is unavailable.
        Currently always returns ``None`` (stub).
    """
    # TODO (v0.3): build a prompt from vibe_label + keywords, call GenAI API,
    # upload/return the resulting image URL.
    return None

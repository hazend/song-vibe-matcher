'''
This is a test file to test the sentiment analysis of lyrics.

For the purpose of MVP, use VADER Sentiment Analysis, since it is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.

In the future, we can use Hugging Face Transformers library for more accurate sentiment analysis.   

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a rule-based, open-source sentiment analysis tool specifically designed for social media text. 
It uses a predefined lexicon (dictionary) of words, mapping them to intensity scores, to classify text as positive, negative, or neutral based on both polarity and intensity.
'''

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def test_vader():
    analyzer = SentimentIntensityAnalyzer()
    lyrics = "I love this beautiful world and everything in it!"
    scores = analyzer.polarity_scores(lyrics)
    print(f"Lyrics: {lyrics}")
    print(f"Scores: {scores}")

    lyrics_sad = "I am so sad and lonely in this dark room."
    scores_sad = analyzer.polarity_scores(lyrics_sad)
    print(f"Lyrics: {lyrics_sad}")
    print(f"Scores: {scores_sad}")

if __name__ == "__main__":
    test_vader()

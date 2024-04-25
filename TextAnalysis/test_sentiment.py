from textblob import TextBlob
import pytest
from sentiment import calculate_sentiment_tone

# Unit tests

def test_positive_sentiment():
    text = "I love this beautiful day"
    sentiment = calculate_sentiment_tone(text)
    assert sentiment > 0, "The sentiment should be positive"

def test_negative_sentiment():
    text = "I hate this dreadful weather"
    sentiment = calculate_sentiment_tone(text)
    assert sentiment < 0, "The sentiment should be negative"

def test_neutral_sentiment():
    text = "This is a pen"
    sentiment = calculate_sentiment_tone(text)
    assert sentiment == 0, "The sentiment should be neutral"

def test_empty_string():
    text = ""
    sentiment = calculate_sentiment_tone(text)
    assert sentiment == 0, "The sentiment for an empty string should be neutral"

def test_non_string_input():
    text = 12345
    with pytest.raises(TypeError):
        calculate_sentiment_tone(text)

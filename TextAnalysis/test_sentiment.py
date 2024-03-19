import pytest
from unittest.mock import patch
from sentiment import calculate_sentiment_tone

@pytest.mark.parametrize("polarity,expected_result", [
    (0.1, 1),  # Positive sentiment
    (-0.1, -1),  # Negative sentiment
    (0.0, 0)  # Neutral sentiment
])

def test_calculate_sentiment_tone(polarity, expected_result):
    with patch('sentiment.spacy.load') as mock_load:
        mock_nlp = mock_load.return_value
        mock_blob = mock_nlp.return_value._.blob
        mock_blob.polarity = polarity
        result, _ = calculate_sentiment_tone("Test text")
        assert result == expected_result

@pytest.mark.parametrize("text,expected", [
    ("This is fantastic!", 1),  # Clearly positive
    ("This is terrible.", -1),  # Clearly negative
    ("", 0),  # Empty string
    ("这是一个测试", 0)  # Non-English text
])
def test_varied_texts(text, expected):
    result, _ = calculate_sentiment_tone(text)
    assert result == expected

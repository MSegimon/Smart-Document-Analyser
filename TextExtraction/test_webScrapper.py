# test_webScrapper.py
import pytest
from unittest.mock import patch
from webScrapper import scrape_article_content

@pytest.mark.parametrize("status_code,expected", [
    (200, [('h1', 'Example Title'), ('p', 'Example paragraph.')]),  # Success case
    (404, "Failed to retrieve the article.")  # Failed request case
])

def test_scrape_article_content(status_code, expected):
    with patch('webScrapper.requests.get') as mock_get:
        mock_get.return_value.status_code = status_code
        if status_code == 200:
            mock_get.return_value.content = '<h1>Example Title</h1><p>Example paragraph.</p>'
        assert scrape_article_content('http://example.com/') == expected

def test_empty_content():
    with patch('webScrapper.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = ''
        assert scrape_article_content('http://example.com/empty') == []

def test_non_standard_structure():
    with patch('webScrapper.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = '<div>Non-standard content without h or p tags.</div>'
        assert scrape_article_content('http://example.com/non-standard') == []

def test_mixed_content_structure():
    with patch('webScrapper.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = '<h1>Title</h1><p>Paragraph 1</p><div>Div content</div><p>Paragraph 2</p>'
        expected = [('h1', 'Title'), ('p', 'Paragraph 1'), ('p', 'Paragraph 2')]
        assert scrape_article_content('http://example.com/mixed') == expected

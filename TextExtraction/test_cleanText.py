# test_cleanText.py
import pytest
from cleanText import filter_content, generate_json_from_content

def test_filter_content():
    content = [('h1', 'Heading'), ('p', 'Short'), ('p', 'Valid paragraph with sufficient length, the length does have to be pretty long for it to count though.')]
    expected = [('h1', 'Heading'), ('p', 'Valid paragraph with sufficient length, the length does have to be pretty long for it to count though.')]
    assert filter_content(content) == expected

def test_generate_json_from_content():
    content = [('h1', 'Main Heading'), ('p', 'Paragraph under main heading.')]
    expected = [
        {"tag": "h1", "text": "Main Heading", "content": [
            {"tag": "p", "text": "Paragraph under main heading.", "content": []}
        ]}
    ]
    assert generate_json_from_content(content) == expected

def test_empty_filter_content():
    assert filter_content([]) == []

def test_all_short_paragraphs():
    content = [('p', 'Short 1'), ('p', 'Short 2')]
    assert filter_content(content) == []

def test_trailing_headings_removed():
    content = [('h1', 'Heading'), ('p', 'Valid paragraph with sufficient length, the length does have to be pretty long for it to count though.'), ('h2', 'Trailing heading')]
    expected = [('h1', 'Heading'), ('p', 'Valid paragraph with sufficient length, the length does have to be pretty long for it to count though.')]
    assert filter_content(content) == expected

def test_deeply_nested_json():
    content = [('h1', 'H1'), ('h2', 'H2'), ('p', 'P under H2'), ('h3', 'H3'), ('p', 'P under H3')]
    expected = [
        {"tag": "h1", "text": "H1", "content": [
            {"tag": "h2", "text": "H2", "content": [
                {"tag": "p", "text": "P under H2", "content": []},
                {"tag": "h3", "text": "H3", "content": [
                    {"tag": "p", "text": "P under H3", "content": []}
                ]}
            ]}
        ]}
    ]
    assert generate_json_from_content(content) == expected
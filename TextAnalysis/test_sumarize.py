import pytest
import spacy
from unittest.mock import patch
from sumarize import extractKeywordsNormalized, summarize

def test_extract_keywords_normalized():
    # Mock or simulate spacy functionality for test simplicity
    test_doc = "This is a test. This document is a test document."
    expected = {"test": 1.0, "document": 1.0}
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(test_doc)
    result = extractKeywordsNormalized(doc)
    assert result == expected

def test_summarize():
    test_text = "This is a test. This document is a test document."
    expected_summary = "This document is a test document."
    result = summarize(test_text)
    assert result == expected_summary

def test_very_short_text():
    text = "Short text."
    expected = ""
    assert summarize(text) == expected

def test_text_lacking_punctuation():
    text = "This is a test This document is a test document"
    expected = ""
    result = summarize(text)
    assert result == expected

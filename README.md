# Smart-Document-Analyser

Smart Document Analyser is a Python package that combines web scraping, text extraction, sentiment analysis, and text summarization functionalities. It provides a comprehensive toolkit for extracting textual content from web articles, analyzing the sentiment of the text, and generating concise summaries. The package is designed to be easy to use and integrate into various applications for content analysis and information retrieval.

## API
The Smart Document Analyser package provides a simple API, built using fastAPI for interacting with its modules. The API includes functions for extracting content from web articles, analyzing the sentiment of text, and generating summaries. Below are the main functionalities provided by the API:
- **Text Extraction**: Extract content from web articles by providing a URL.
- **Sentiment Analysis**: Analyze the sentiment of a given text and determine if it is positive, negative, or neutral.
- **Text Summarization**: Generate a concise summary of a text by identifying key points and significant sentences.
- **CRUD Operations**: Perform CRUD operations on user data and text files.

### Installation
Before running the API, ensure you have Python 3.10 or higher installed. You can install the required dependencies using pip and the provided `requirements.txt` file:
```sh
pip install -r requirements.txt
```

### Running the API
To start the API server, run the following command:
```sh
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. You can access the interactive API documentation (Swagger UI) at `http://localhost:8000/docs`.

## Modules
The Smart Document Analyser package consists of two main modules: Text Extraction and Text Analysis. These modules provide functionalities for extracting content from web articles, analyzing the sentiment of text, and generating summaries. They can be used independently or together to perform various text processing tasks. Below is an overview of each module:

### Text Extraction Module

#### Overview
The Text Extraction Module is a Python package designed for scraping, cleaning, and structuring textual content from web articles. It leverages `requests` and `BeautifulSoup` for web scraping, and provides a structured JSON output of the article content, making it easier for further processing or analysis.

#### Features
- Web scraping of article content using URL.
- Filtering of content to remove short paragraphs and trailing headings.
- Structuring the cleaned content into a nested JSON format based on headings and paragraphs.

#### Installation
Before installing the Text Extraction Module, ensure you have Python 3.6 or higher installed. This module depends on `requests` and `BeautifulSoup` libraries. You can install the module and its dependencies using pip:

```sh
pip install requests beautifulsoup4
```

#### Usage
##### Extracting Content from a URL
To extract content from a web article, you can use the `extract_content` function from the `extractContent.py` module. This function requires a URL string as an argument:

```python
from extractContent import extract_content

url = 'http://example.com/article'
content_json = extract_content(url)
print(content_json)
```

##### Structure of the JSON Output
The JSON output is structured as a list of dictionaries, each representing a section of the article. Headings are considered as starting points for sections, with paragraphs as content. Nested sections are represented as nested lists within the JSON structure.

#### Modules
The package consists of the following modules:
- `webScrapper.py`: Contains the `scrape_article_content` function for scraping content from the given URL.
- `cleanText.py`: Contains the `filter_content` and `generate_json_from_content` functions for cleaning the scraped content and structuring it into JSON format.
- `extractContent.py`: The main module that integrates scraping, cleaning, and structuring functionalities.

#### Testing
The package includes test modules for both the web scraping (`test_webScrapper.py`) and content cleaning (`test_cleanText.py`) functionalities. These tests can be run using pytest:

```sh
pytest test_webScrapper.py
pytest test_cleanText.py
```

### Text Analysis Module

#### Overview
The Text Analysis Module is a comprehensive Python toolkit for performing sentiment analysis and summarization on textual data. Utilizing the power of `spaCy` and its extensions, this module offers easy-to-use functions for deriving sentiment tone and generating concise summaries of larger texts. It's suitable for analyzing content ranging from articles and reports to user feedback and social media posts.

#### Features
- **Sentiment Analysis**: Determine the overall sentiment of a text as positive, negative, or neutral.
- **Text Summarization**: Automatically generate a summary of a text, focusing on its key points.

### Installation
Ensure you have Python 3.6 or higher installed before using the Text Analysis Module. This module requires `spaCy`, `spacytextblob`, and potentially other language models for `spaCy`. Install them using pip:

```sh
pip install spacy spacytextblob
python -m spacy download en_core_web_sm
```

#### Usage
##### Sentiment Analysis
To analyze the sentiment of a given text, use the `calculate_sentiment_tone` function from the `sentiment.py` module. This function returns the sentiment tone as `-1` for negative, `1` for positive, and `0` for neutral sentiments:

```python
from sentiment import calculate_sentiment_tone

text = "This is a great day!"
sentiment_tone, _ = calculate_sentiment_tone(text)
print(sentiment_tone)  # Output: 1 for positive sentiment
```

##### Text Summarization
For summarizing a text, utilize the `summarize` function from the `sumarize.py` module. It generates a concise summary by identifying and extracting the most significant sentences:

```python
from sumarize import summarize

text = "Your long text here..."
summary = summarize(text)
print(summary)
```

#### Components
This package comprises:
- `sentiment.py`: Implements the sentiment analysis functionality.
- `sumarize.py`: Implements the text summarization functionality.

#### Testing
Test modules `test_sentiment.py` and `test_sumarize.py` are included to ensure reliability. Run these tests using pytest to verify the correctness of sentiment analysis and summarization functionalities:

```sh
pytest
```

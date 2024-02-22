import requests
from bs4 import BeautifulSoup

def scrape_article_content(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # Initialize a list to hold the scraped content in order
        article_content_ordered = []
        
        # Extract all relevant tags (headings and paragraphs)
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
            article_content_ordered.append((tag.name, tag.get_text(strip=True)))
        
        return article_content_ordered
    else:
        return "Failed to retrieve the article."

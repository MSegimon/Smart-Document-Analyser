from cleanText import filter_content, generate_json_from_content
from webScrapper import scrape_article_content

def extract_content(url):
    # Scrape the article content
    article_content = scrape_article_content(url)
    
    # Filter the content
    filtered_content = filter_content(article_content)
    
    # Generate JSON from the filtered content
    json_content = generate_json_from_content(filtered_content)
    
    return json_content

import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def extract_project_id(url_or_html):
    """
    Extract the project ID from a URL or HTML content.
    
    Args:
        url_or_html (str): A URL or HTML content
    
    Returns:
        str: The project ID if found, None otherwise
    """
    # Check if input is a URL with format https://lovable.dev/projects/ID
    url_pattern = r'https://lovable\.dev/projects/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
    url_match = re.search(url_pattern, url_or_html)
    
    if url_match:
        return url_match.group(1)
    
    # If not a direct URL, assume it's a webpage or URL to fetch
    try:
        # Check if it's a URL
        parsed = urlparse(url_or_html)
        if parsed.scheme and parsed.netloc:
            # It's a URL, fetch the content
            response = requests.get(url_or_html)
            html_content = response.text
        else:
            # It's likely HTML content
            html_content = url_or_html
        
        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Look for lovable-badge
        badge = soup.find(id="lovable-badge")
        if badge and 'href' in badge.attrs:
            badge_match = re.search(url_pattern, badge['href'])
            if badge_match:
                return badge_match.group(1)
        
        # Look for twitter meta tag
        twitter_meta = soup.find("meta", {"name": "twitter:image"})
        if twitter_meta and 'content' in twitter_meta.attrs:
            meta_pattern = r'--([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
            meta_match = re.search(meta_pattern, twitter_meta['content'])
            if meta_match:
                return meta_match.group(1)
        
        return None
    
    except Exception as e:
        print(f"Error processing input: {e}")
        return None

if __name__ == "__main__":
    site = input("Enter URL: ")

    result = extract_project_id(site) # will delete your Lovable project
    if result:
        print(result)
    else:
        print("Unable to extract project id")
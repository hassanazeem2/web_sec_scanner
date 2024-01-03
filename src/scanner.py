import requests
from bs4 import BeautifulSoup

def fetch_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error getting URL: {e}")
        return None
    

def crawl_and_scan(url):
    content = fetch_url_content(url)

    if content:

        soup = BeautifulSoup(content, 'html.parser')

        print(f"Title of {url}: {soup.title.string}")
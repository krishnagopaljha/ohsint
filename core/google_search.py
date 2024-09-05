# core/google_search.py
import requests
from bs4 import BeautifulSoup

def google_search(query):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
        results = [result.get_text() for result in search_results]
        return results
    except Exception as e:
        return f"Error: {e}"

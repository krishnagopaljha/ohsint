import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

def sanitize_filename(url):
    """Sanitize the URL to create a valid filename."""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith('www.'):
        domain = domain[4:]
    domain = re.sub(r'\..*$', '', domain)
    return domain

class TechnologyDetector:
    def __init__(self, csv_file):
        self.technologies = self.load_technologies(csv_file)

    def load_technologies(self, csv_file):
        """Load technologies from CSV file."""
        tech_data = {}
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    category = row['category']
                    subcategory = row['subcategory']
                    tech = row['technology']
                    identifier = row['identifier'].lower()
                    if category not in tech_data:
                        tech_data[category] = {}
                    if subcategory not in tech_data[category]:
                        tech_data[category][subcategory] = []
                    tech_data[category][subcategory].append((identifier, tech))
                except KeyError as e:
                    print(f"KeyError: Missing column in CSV file - {e}")
                    raise
        return tech_data

    def detect_technologies(self, url):
        """Detect technologies used on a given URL."""
        retries = 3
        detected_technologies = {cat: {subcat: [] for subcat in techs.keys()} for cat, techs in self.technologies.items()}
        
        for attempt in range(retries):
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                headers = response.headers
                content = response.text.lower()

                for category, subcategories in self.technologies.items():
                    for subcategory, techs in subcategories.items():
                        for identifier, tech in techs:
                            if identifier in content:
                                detected_technologies[category][subcategory].append(tech)

                # Check for web servers
                server = headers.get('Server', '').lower()
                if 'apache' in server:
                    detected_technologies.setdefault('Hosting and Servers', {}).setdefault('Web Servers', []).append("Apache")
                if 'nginx' in server:
                    detected_technologies.setdefault('Hosting and Servers', {}).setdefault('Web Servers', []).append("Nginx")
                if 'iis' in server:
                    detected_technologies.setdefault('Hosting and Servers', {}).setdefault('Web Servers', []).append("IIS")

                # Return detected technologies
                return detected_technologies
            except requests.RequestException as e:
                print(f"[-] Error detecting technologies (attempt {attempt + 1}/{retries}): {e}")
                if attempt < retries - 1:
                    print("Retrying...")
                else:
                    print("Website might not exist or may not be available at this moment.")
        return detected_technologies

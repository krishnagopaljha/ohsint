# core/domain_lookup.py
import whois
import requests
from bs4 import BeautifulSoup
import re

# Function to extract email addresses using regex
def extract_emails(text):
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_regex, text)

# Function to extract phone numbers using regex (international format)
def extract_phone_numbers(text):
    phone_regex = r'\+?\d[\d -]{8,13}\d'
    return re.findall(phone_regex, text)

# Function to scan website for emails and phone numbers
def scan_website(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()  # Extract all text from the website

            # Find potential contact information
            emails = extract_emails(text)
            phone_numbers = extract_phone_numbers(text)

            contact_info = {
                "emails": emails,
                "phone_numbers": phone_numbers
            }
            return contact_info
        else:
            return {"error": f"Unable to fetch the website: {domain}"}
    except Exception as e:
        return {"error": f"Error scanning the website: {e}"}

def domain_lookup(domain):
    try:
        # Perform WHOIS lookup
        domain_info = whois.whois(domain)
        
        # Scan the website for potential contact information
        contact_info = scan_website(domain)

        result = {
            "whois_info": domain_info,
            "contact_info": contact_info
        }
        return result
    except Exception as e:
        return {"error": f"Error during WHOIS lookup: {e}"}

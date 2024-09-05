# core/ip_lookup.py
import requests

def ip_lookup(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: Unable to fetch details for IP {ip}"
    except Exception as e:
        return f"Error: {e}"

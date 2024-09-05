import os
import json
from core.phone_lookup import phone_lookup
from core.domain_lookup import domain_lookup
from core.ip_lookup import ip_lookup
from core.google_search import google_search
from core.address_geocoding import geocode_address
from core.techstack import TechnologyDetector
from core.ssl_certificate_check import get_certificate_details, parse_certificate

def logo():
    """Return the logo text."""
    return """
  ____  _    _  _____ _____ _   _ _______ 
 / __ \| |  | |/ ____|_   _| \ | |__   __|
| |  | | |__| | (___   | | |  \| |  | |   
| |  | |  __  |\___ \  | | | . ` |  | |   
| |__| | |  | |____) |_| |_| |\  |  | |   
 \____/|_|  |_|_____/|_____|_| \_|  |_|  

|--------------------------------------------------------------------|
| Created By: Krishna Gopal Jha                                      |
| Checkout my LinkedIn: https://www.linkedin.com/in/krishnagopaljha/ |
| Lookup at my insta: https://instagram.com/theindianpsych           |
|--------------------------------------------------------------------|
    """

def clear_screen():
    """Clear the terminal screen and set text color to green."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92m", end='')  # Green color for terminal text

def print_centered(text):
    """Print text centered on the terminal screen."""
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size.columns
    lines = text.split('\n')
    for line in lines:
        print(line.center(terminal_width))

def print_menu():
    """Print the main menu."""
    menu_text = """
Select an option:
1. Domain Lookup
2. IP Lookup
3. Google Search
4. Address Geocoding
5. Technology Stack Detection
6. SSL/TLS Certificate Details
7. Exit
    """
    print_centered(menu_text)

def main():
    """Main interactive loop."""
    clear_screen()
    print_centered(logo())

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            domain = input("Enter the domain to lookup: ")
            result = domain_lookup(domain)
            print_centered(json.dumps(result, default=str, indent=4, sort_keys=True))
        elif choice == '2':
            ip = input("Enter the IP address to lookup: ")
            result = ip_lookup(ip)
            print_centered(json.dumps(result, default=str, indent=4, sort_keys=True))
        elif choice == '3':
            query = input("Enter the Google search query: ")
            result = google_search(query)
            print_centered(json.dumps(result, default=str, indent=4, sort_keys=True))
        elif choice == '4':
            address = input("Enter the address to geocode: ")
            result = geocode_address(address)
            print_centered(json.dumps(result, default=str, indent=4, sort_keys=True))
        elif choice == '5':
            url = input("Enter the URL to detect technologies: ")
            detector = TechnologyDetector('data/technologies.csv')
            result = detector.detect_technologies(url)
            print_centered(json.dumps(result, default=str, indent=4, sort_keys=True))
        elif choice == '6':
            domain = input("Enter the domain to check SSL/TLS certificate: ")
            cert = get_certificate_details(domain)
            result = parse_certificate(cert)
            print_centered(json.dumps(result, default=str, indent=4, sort_keys=True))
        elif choice == '7' or 'exit':
            print_centered("Exiting...")
            break
        else:
            print_centered("Invalid choice, please select a number between 1 and 7.")

if __name__ == "__main__":
    main()

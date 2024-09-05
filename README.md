# OH$INT

A comprehensive OSINT (Open Source Intelligence) tool for gathering and analyzing information from various sources. This tool supports domain lookup, IP lookup, Google search, address geocoding, technology stack detection, and SSL/TLS certificate details.

## Features

- **Domain Lookup**: Retrieve WHOIS information and check domain availability.
- **IP Lookup**: Get details about an IP address including geolocation.
- **Google Search**: Perform Google searches and retrieve results.
- **Address Geocoding**: Convert physical addresses into geographic coordinates.
- **Technology Stack Detection**: Identify technologies used on a website.
- **SSL/TLS Certificate Details**: Obtain and parse SSL/TLS certificate information.

## Requirements

- Python 3.x
- Required Python packages are listed in `requirements.txt`.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/krishnagopaljha/ohsint.git
   cd osint-tool
   ```
2. **Install Dependenciesy**

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   ## Usage

   1. Run the Tool

      Execute app.py to start the interactive mode:

      ```bash
      python app.py
      ```

   2. Interactive Menu

      Interactive Menu
      - **1. Domain Lookup**: Enter a domain to retrieve WHOIS information and check availability.
      - **2. IP Lookup**: Enter an IP address to get its details.
      - **3. Google Search**: Enter a search query to perform a Google search.
      - **4. Address Geocoding**: Enter an address to get its geographic coordinates.
      - **5. Technology Stack Detection**: Enter a URL to detect technologies used on the website.
      - **6. SSL/TLS Certificate Details**: Enter a domain to check SSL/TLS certificate details.
      - **7. Exit**: Exit the tool.

     3. Input Prompts

        Follow the prompts to input the necessary information for each feature. Results will be displayed directly in the            terminal.

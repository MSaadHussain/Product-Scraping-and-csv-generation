# Product Scraping and csv generation
Product Extraction script for custom e commerce websites  , custom script made in python

**This script is designed to scrape product information from a specific webpage, process the data, and store it in a CSV file**. The script uses the "requests" library to retrieve webpage content and the "BeautifulSoup" library for HTML parsing.

# Features
Scrapes product information including title, short descriptions, long descriptions, images, categories, and prices from a given webpage.
Processes and formats the data as needed before saving it to a CSV file.
Downloads images and saves them to a local folder.
Calculates updated prices based on a predefined formula.
Appends the scraped data to an existing CSV file or creates a new one if it doesn't exist.

# Requirements
Python 3.x
# Python libraries
requests library: To make HTTP requests
BeautifulSoup library: For HTML parsing
csv module: For working with CSV files

# Configuration
You can customize the scraping behavior by modifying the script's parameters and HTML element classes.
Ensure you have the correct HTML classes for the elements you're trying to scrape.
Update the link_to_upload variable to the appropriate image upload location if needed.

# Disclaimer
This script is provided as-is and may require adjustments to work with specific websites. Be mindful of the website's terms of use and scraping policies.

# Imports
import requests
from bs4 import BeautifulSoup

# Send request to URL
url = "https://learncodinganywhere.com/"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract the page title
title_element = soup.find("title")
if title_element:
    title = title_element.text
    print("Page Title:", title)
else:
    print("Page title not found")
import requests
import json
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        print("Fetching URL...")
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        print("URL fetched successfully.")

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the script tag containing the JSON data
        script_tag = soup.find('script', attrs={'id': '__NEXT_DATA__'})
        if not script_tag:
            return "No script tag with id '__NEXT_DATA__' found."

        # Extract and parse the JSON string from the script tag
        json_data = json.loads(script_tag.string)
        return json_data

    except requests.RequestException as e:
        return f"HTTP request error: {e}"
    except json.JSONDecodeError:
        return "Error decoding JSON"
    except Exception as e:
        return f"An error occurred: {e}"

# URL of the webpage to scrape
url = 'https://www.zillow.com/'

# Fetch and print the data using the fetch_data function
data = fetch_data(url)
print(data)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/'
}
response = requests.get(url, headers=headers)
session = requests.Session()
session.headers.update(headers)
response = session.get(url)
import time

time.sleep(1)  # Sleep for 1 second between requests
response = session.get(url)
print(response.status_code)
print(response.headers)
print(response.text[:500])  # print the first 500 characters of the response text

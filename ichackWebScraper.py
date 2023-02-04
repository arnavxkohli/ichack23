import requests
from bs4 import BeautifulSoup

def search_google(keyword):
    # Make a GET request to Google to search for the keyword
    response = requests.get(f"https://www.google.com/search?q={keyword}")
    
    # Use BeautifulSoup to parse the HTML of the response
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all the search result links
    result_links = soup.find_all("a")
    
    # Extract the URLs from the links and print them
    for link in result_links:
        url = link.get("href")
        if url.startswith("/url?q="):
            print(url[7:])

# Example usage: search for "python programming"
search_google("chicken recipe")

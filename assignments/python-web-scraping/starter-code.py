import csv
import requests
from bs4 import BeautifulSoup

URL = "https://example.com"

def fetch_page(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")

def extract_items(soup: BeautifulSoup):
    # Example: extract all links from the page
    return [
        {
            "text": a.get_text(strip=True),
            "url": a["href"],
        }
        for a in soup.select("a[href]")
    ]

def save_results(items, filename: str = "results.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["text", "url"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)
s
if __name__ == "__main__":
    html = fetch_page(URL)
    soup = parse_html(html)
    items = extract_items(soup)
    save_results(items)
    print(f"Saved {len(items)} items to results.csv")

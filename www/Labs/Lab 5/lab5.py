from bs4 import BeautifulSoup
import requests

website_url = "https://www.brown.edu/about/administration/registrar/academic-calendar"
calendar_page = BeautifulSoup(
   requests.get(website_url).content, features="html.parser"
)


def scrape_events(page: BeautifulSoup) -> dict:
   # TODO: Write function that creates a dict (key is date and value is event name)
   pass

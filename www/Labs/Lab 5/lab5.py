from bs4 import BeautifulSoup
import requests

calendar_url = "https://www.brown.edu/about/administration/registrar/academic-calendar"
calendar_page = BeautifulSoup(
   requests.get(calendar_url).content, features="html.parser"
)


def scrape_events(page: BeautifulSoup) -> dict:
   # TODO: Write function that creates a dict (key is date and value is event name)
   pass

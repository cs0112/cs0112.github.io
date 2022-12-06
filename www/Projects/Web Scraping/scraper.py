import requests
from bs4 import BeautifulSoup

"""
Place your answers to the Design check questions here:

1.

2.

3.

4.

"""

CITIES = [
    "providence",
    "atlanta",
    "austin",
    "boston",
    "chicago",
    "dallas",
    "denver",
    "detroit",
    "houston",
    "lasvegas",
    "losangeles",
    "miami",
    "minneapolis",
    "newyork",
    "philadelphia",
    "phoenix",
    "portland",
    "raleigh",
    "sacramento",
    "sandiego",
    "seattle",
    "washingtondc",
]


class NoCityError(Exception):
    pass

def craigslist_get_city(city_name) -> BeautifulSoup:
    """Returns a BeautifulSoup object for a given city from Craigslist"""
    url_template = "https://{}.craigslist.org/search/apa"
    try:
        resp = requests.get(url_template.format(city_name))
        return BeautifulSoup(resp.content, "html.parser")
    except:
        raise NoCityError("No city named {} found".format(city_name))


def local_get_city(city_name) -> BeautifulSoup:
    """Returns a BeautifulSoup object for a given city from the local filesystem"""
    file_template = "localdata/{}.html"
    try:
        with open(file_template.format(city_name), "r") as f:
            return BeautifulSoup(f.read(), "html.parser")
    except:
        raise NoCityError("No city named {} found".format(city_name))

def scrape_data(city_pages: dict):
    """Scrapes data from a collection of pages.
    The keys of city_pages are city names. The values are BeautifulSoup objects."""
    pass

def scrape_craigslist_data():
    """Scrape data from Craigslist"""
    return scrape_data({city: craigslist_get_city(city) for city in CITIES})


def summarize_local_data():
    """Scrape data from the local filesystem"""
    return scrape_data({city: local_get_city(city) for city in CITIES})


def interesting_word(word: str) -> bool:
    """Determines whether a word in a listing is interesting"""
    return word.isalpha() and word not in [
        "to",
        "at",
        "your",
        "you",
        "and",
        "for",
        "in",
        "the",
        "with",
        "bedroom",
        "bed",
        "bath",
        "unit",
    ]
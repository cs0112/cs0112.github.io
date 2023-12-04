from bs4 import BeautifulSoup
# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Place your answers to the Design check questions here:

1.

2.

3.

4.

"""
################## CHROME ################### 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """Change only if you are using a different browser. Default on the stencil is google chrome."""
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)
############################################# 

##################### DO NOT CHANGE #######################

def craigslist_get_city(city_name: str, driver: webdriver):
    """Returns a BeautifulSoup object for a given city from Craigslist"""


    url = f"https://{city_name}.craigslist.org/search/apa"
    driver.get(url)

    ## The difference here from previous webscraping examples done in lab/class is this one step!
    ## Instead of using requests, we will be using a driver. 
    try:
        # WebDriverWait with EC is used to stop program execution temporarily 
        # until the specified condition is met or the maximum wait time is reached
        # Here, we wait up to 10 seconds before timing out if it does not find the elements with the class name 'result-title'.
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "result-title"))
        )
    except Exception as e:
        print("Exception while waiting for page elements:", e)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def local_get_city(city_name: str) -> BeautifulSoup:
    """Returns a BeautifulSoup object for a given city from the local filesystem"""

    # Files must be in this directory
    file_template = "localdata/{}.html"
    try:
        with open(file_template.format(city_name), "r") as f:
            return BeautifulSoup(f.read(), "html.parser")
    except:
        raise NoCityError("No city named {} found".format(city_name))
##################### DO NOT CHANGE #######################


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

def scrape_data(city_pages: dict):
    """Scrapes data from a collection of pages.
    The keys of city_pages are city names. The values are BeautifulSoup objects."""
    pass

def scrape_craigslist_data():
    """Scrape data from Craigslist"""
    return scrape_data({city: craigslist_get_city(city, get_driver()) for city in CITIES})


def scrape_local_data():
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

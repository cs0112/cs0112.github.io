import requests
from typing import List, Dict
from dataclass import dataclass

@dataclass
class BDRItem:
   #TODO: Fill this dataclass out


##################### API IMPLEMENTATION #######################
def get_collectionids() -> dict[str : str]:
    """
    Returns a dictionary of collection names to collection ids.
    """
    pass


def collection_request(collection_id: str):
    """
    Returns the json for the collection.
    """
    pass


def get_theses_collections(collection_id: str):
    """
    Returns a list of all the theses collections in the BDR.
    """
    pass


def item_request(item_id: str):
    """
    Returns the json for the given item id.
    """
    pass


def scrape_item(response: Any) -> BDRItem:
    """
    Creates an item from an item page.
    """
    pass


def get_items_from_collection(response) -> list[BDRItem]:
    """
    Returns a list of items from a collection.
    """
    pass


def api_data(collection_dict: dict[str: str]) -> dict[str: list[BDRItem]]:
    """
    Returns a dictionary of items from the collections.
    """
    pass


##################### SEARCH IMPLEMENTATION #######################

def search_request(params: dict):
    """
    Returns the json for the search results.
    """
    pass


def search_data(params: dict) -> dict[str: list[BDRItem]]:
    """
    Returns a dictionary of search results.
    """
    pass


##################### QUERY FUNCTIONS #######################

def most_common_subject(data):
    """
    Returns the most common subject in the data.
    """
    pass


def year_after(data):
    """
    Returns the number of items published after the given year.
    """
    pass


def top_contributor(data):
    """
    Returns the top contributor in the data.
    """
    pass


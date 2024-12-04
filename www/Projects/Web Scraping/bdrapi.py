import requests
from typing import Any, Dict, List
from common import BDRItem

BASE_URL = "https://repository.library.brown.edu/api/"

##################### API IMPLEMENTATION #######################
def get_collectionids() -> Dict[str : str]:
    """
    Returns a dictionary of collection names to collection ids.
    """
    # Hint: Use the requests library to get the data from the URL
    # Then, use the .json() method to convert the response to a dictionary
    # Print the json_response to understand the structure of the data
    pass


def collection_request(collection_id: str):
    """
    Returns the json for the collection.
    """
    pass


def get_theses_collections(num_theses: int = 50) -> Dict[str: str]:
    """
    Returns a list of all the theses collections in the BDR that have less than 50 items.

    :param num_theses: The maximum number of theses in the collection (default 50)
    :return: Dictionary of the collection names to the collection IDs
    """
    collection_ids = get_collectionids()
    theses_collections = {}
    for collection_id in collection_ids.values():
        json_response = collection_request(collection_id)
        name = json_response["name"]
        child_folders = json_response["child_folders"]
        for child in child_folders:
            if child["name"] == "Theses and Dissertations":
                theses_collections[name] = child["db_id"]

    filtered_theses = {}
    for name, collection_id in theses_collections.items():
        json_response = collection_request(collection_id)
        if json_response["items"]["numFound"] <= num_theses and json_response["items"]["numFound"] > 0:
            filtered_theses[name] = collection_id

    return filtered_theses


def item_request(item_id: str):
    """
    Returns the json for the given item id.
    """
    # Hint: Request from the item URL and return the json response
    pass


def scrape_item(response: Any) -> BDRItem:
    """
    Creates an item from an item page.
    """
    pass


def get_items_from_collection(response: Any) -> List[BDRItem]:
    """
    Returns a list of items from a collection.
    """
    pass


def api_data(collection_dict: Dict[str: str]) -> Dict[str: List[BDRItem]]:
    """
    Returns a dictionary of items from the collections.
    """
    pass


##################### RUN FUNCTIONS #######################

def run_api():
    """
    Runs the API implementation.
    """
    data = api_data(get_theses_collections())
    return data

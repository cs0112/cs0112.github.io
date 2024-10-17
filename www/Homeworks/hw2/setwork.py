import json
from typing import Dict, Set


def add_user(users: dict, name: str) -> None:
    """
    Adds a user to the data with no interests.
    """
    pass


def add_interest(users: dict, name: str, interest: str) -> None:
    """
    Adds an interest for the named user.
    """
    pass


def copy_interests(users: dict, name_to: str, name_from: str) -> None:
    """
    Adds all of name_from's interests to name_to.
    """
    pass


def interest_exists(users: dict, interest: str) -> bool:
    """
    Returns True if any user has this interest, False otherwise.
    """
    pass


def interests_match(users: dict, name: str, n: int) -> set:
    """
    Returns a set of all users who share at least n 
    interests with the named user
    """
    pass


def remove_user(users: dict, name: str) -> dict:
    """
    Returns a dictionary with the target user removed.
    """
    pass


"""
DO NOT EDIT BELOW THIS LINE EXCEPT WHERE ASKED TO
"""
def load_json_to_dict(data: dict, name: str) -> dict:
    """
    Loads user interests from JSON data into a dictionary.
    
    :param data: The JSON data.
    :param name: The name of the user.
    :return: A dictionary with the user's interests.
    """
    user_interests = {name: set()}
    for topic in data["topics_your_topics"]:
        interest = topic["string_map_data"]["Name"]["value"]
        user_interests[name].add(interest)
    return user_interests

# Load data from JSON file
with open("your_topics.json", "r") as f:
    data = json.load(f)


"""
Dear user, please write the name of your favorite artist here. (DO NOT WRITE YOUR REAL NAME)
"""
# Initialize users dictionary
users = load_json_to_dict(data, "Your favorite artist's name here")
print(users)

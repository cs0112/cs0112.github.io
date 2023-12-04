import json

def add_user(users: dict, name: str):
    """adds a user to the data with no interests"""
    pass

def add_interest(users: dict, name: str, interest: str):
    """adds an interest for the named user"""
    pass

def copy_interests(users: dict, name_to: str, name_from: str):
    """adds all of name_from's interests to name_to"""
    pass

def interest_exists(users: dict, interest: str) -> bool:
    """returns True if any user has this interest, False otherwise"""
    pass

def interests_match(users: dict, name: str, n: int) -> set:
    """returns a set of all users who share at least n 
       interests with the named user"""
    pass

def remove_user(users: dict, name: str) -> dict:
    """returns a dictionary with the target user removed"""
    pass


"""
DO NOT EDIT BELOW THIS LINE EXCEPT WHERE ASKED TO
"""
t = open ("your_topics.json")
data = json.load(t)
t.close()

def load_json_to_dict(data: dict, name: str) -> dict:
    dict = {}
    dict[name] = set ()
    for i in data["topics_your_topics"][:5]:
        interest = i['string_map_data']['Name']['value']
        dict[name].add(interest)
    return dict

"""
Dear user, please write the name of your favorite artist here. (DO NOT WRITE YOUR REAL NAME)
"""
users = load_json_to_dict(data,"Your favorite artist's name here")
print(users)
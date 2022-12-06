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

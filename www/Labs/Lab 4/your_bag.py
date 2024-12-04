from typing import List

class BagItem:
    """Base class for all items in the bag."""
    def __init__(self):
        self.is_item = True

    def is_ticket(self, country_name: str) -> bool:
        """
        Check if the item is a ticket for the specified country.
        This method should be overridden by subclasses.
        """
        return False

class FlightTicket(BagItem):
    def __init__(self, country_name: str, departure_time: int):
        super().__init__()
        self.country_name = country_name
        self.departure_time = departure_time

    def read_departure_time(self):
        print(f"Departure time: {self.departure_time}")

    def is_ticket(self, country_name: str) -> bool:
        # TODO: Implement this method to check if this is the correct flight ticket
        pass

class Receipt(BagItem):
    def __init__(self, store_name: str, price: float):
        super().__init__()
        self.store_name = store_name
        self.price = price

    def is_ticket(self, country_name: str) -> bool:
        # TODO: Implement this method (hint: a receipt is never a flight ticket)
        pass

class Phone(BagItem):
    def __init__(self, brand: str, is_on: bool = False):
        super().__init__()
        self.brand = brand
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} phone is now on.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} phone is now off.")

    def is_ticket(self, country_name: str) -> bool:
        # TODO: Implement this method (hint: a phone is never a flight ticket)
        pass

def check_item(item: BagItem, country_name: str) -> bool:
    """
    Check if the given item is a flight ticket for the specified country.
    
    
    : param item (BagItem): The item to check.
    : param country_name (str): The country name to check for.
    : return (bool): True if the item is a flight ticket for the specified country, False otherwise.
    """
    # TODO: Implement this function using the polymorphic is_ticket method
    pass

def search_for_ticket(things_in_bag: List[BagItem]):
    """
    Search through the bag for flight tickets to various countries.
    
    : param things_in_bag (List[BagItem]): A list of items in the bag.
    """
    for item in things_in_bag:
        if check_item(item, "France"):
            print('The flight ticket for France is in the bag!')
        elif check_item(item, "Japan"):
            print('The flight ticket for Japan is in the bag!')
        elif check_item(item, "Germany"):
            print('The flight ticket for Germany is in the bag!')
        else:
            print('This is not the flight ticket.')

# Test the search function
if __name__ == "__main__":
    bag_contents = [
        Receipt("Coffee shop", 13.50),
        Phone("Samsung", False),
        FlightTicket("France", 1400),
        Receipt("Uniqlo", 200.00),
        Receipt("Brown Bookstore", 350.75)
    ]
    
    search_for_ticket(bag_contents)

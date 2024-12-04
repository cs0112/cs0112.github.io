class BagItem:
    def __init__(self):
        self.is_item = True

class FlightTicket(BagItem):
    def __init__(self, country_name: str, departure_time: int):
        self.country_name = country_name
        self.departure_time = departure_time

    def read_departure_time(self):
        print(self.departure_time)

    def is_ticket(self, country_name: str) -> bool:
        return (country_name == self.country_name)

class Receipt(BagItem):
    def __init__(self, store_name: str, price: int):
        self.store_name = store_name
        self.price = price

    def is_ticket(self, country_name: str) -> bool:
        return False

class Phone(BagItem):
    def __init__(self, brand: str, is_on: bool):
        self.brand = brand
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} phone is now on.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} phone is now off.")

    def is_ticket(self, country_name: str) -> bool:
        return False

# checks whether or not the flight ticket with the country name is in the bag
def check_item(item: BagItem, country_name: str) -> bool:  
    """
    Here, you should use the polymorphic is_ticket method defined in the classes above
    in order to see if the current item is the flight ticket or not
    This function will be called in the for loop below to print the result of your check
    """
    return item.is_ticket(country_name)

def search_for_ticket(things_in_bag):
    for item in things_in_bag:
        if check_item(item, "France"):
            print('The flight ticket for France is in the bag!')
        elif check_item(item, "Japan"):
            print('The flight ticket for Japan is in the bag!')
        elif check_item(item, "Germany"):
            print('The flight ticket for Germany is in the bag!')
        else:
            print('This is not the flight ticket')

search_for_ticket([Receipt("Coffee shop", 13), Phone("Samsung", False), FlightTicket("France", 400),
                   Receipt("Uniqlo", 200), Receipt("Brown Bookstore", 350)])

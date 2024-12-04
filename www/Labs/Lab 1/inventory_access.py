import os
import random
from typing import Dict

inventory = {
    "wood": 0,
    "stone": 0,
    "iron": 0,
    "diamond": 0
}

world = {
    "forest": ["wood", "wood", "wood", "stone"],
    "cave": ["stone", "stone", "iron"],
    "mountain": ["stone", "iron", "diamond"]
}

recipes = {
    "wooden_pickaxe": {"wood": 3},
    "stone_pickaxe": {"wood": 2, "stone": 3},
    "iron_pickaxe": {"wood": 2, "iron": 3},
    "diamond_pickaxe": {"wood": 2, "diamond": 3}
}


def collect_resources(biome: str) -> Dict[str, int]:
    """
    Collect resources from the given biome.

    :param biome: The biome to collect resources from.
    :return: Updated inventory after collecting resources.
    """
    pass


def display_inventory() -> None:
    """
    Display the current inventory.
    """
    pass


def craft_item(item: str) -> str:
    """
    Craft the given item.

    :param item: The item to craft.
    :return: A message indicating whether the item was crafted
    """
    pass



# Helper function to clear the terminal screen
def clear_screen():
    # Clear the terminal screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

def main():
    clear_screen()
    while True:
        print("\n--- Pythoncraft ---")
        print("1. Collect resources")
        print("2. View inventory")
        print("3. Craft item")
        print("4. Quit")

        choice = input("What would you like to do? ")

        if choice == "1":
            biome = input("Enter a biome (forest/cave/mountain): ")
            print(collect_resources(biome))
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            item = input("What would you like to craft? ")
            print(craft_item(item))
        elif choice == "4":
            print("Thanks for playing Pythoncraft!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

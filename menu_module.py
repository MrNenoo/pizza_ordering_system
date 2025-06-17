# menu_module.py

import json
import os

MENU_FILE = os.path.join("data", "menu.json")

def load_menu():
    """Loads the menu from the JSON file."""
    with open(MENU_FILE, "r") as f:
        data = json.load(f)
    return data["pizzas"], data["sizes"], data["crusts"], data["toppings"]

def save_menu(pizzas, sizes, crusts, toppings):
    """Save updated menu back to the JSON file."""
    with open(MENU_FILE, "w") as f:
        json.dump({
            "pizzas": pizzas,
            "sizes": sizes,
            "crusts": crusts,
            "toppings": toppings
        }, f, indent=4)


def show_menu():
    """Prints the full pizza menu to the console."""
    pizzas, sizes, crusts, toppings = load_menu()

    print("\n🍕 Pizza Menu:")
    for name, price in pizzas.items():
        print(f"  {name:<20} ₹{price}")

    print("\n📏 Sizes (extra cost):")
    for size, add_price in sizes.items():
        print(f"  {size:<10} +₹{add_price}")

    print("\n🍞 Crust Options (extra cost):")
    for crust, add_price in crusts.items():
        print(f"  {crust:<15} +₹{add_price}")

    print("\n🧀 Toppings (each at extra cost):")
    for topping, add_price in toppings.items():
        print(f"  {topping:<20} +₹{add_price}")
    print()

def get_menu_data():
    """
    Returns all menu dictionaries so other modules can use them.

    :return: tuple of (pizzas, sizes, crusts, toppings)
    """
    return load_menu()

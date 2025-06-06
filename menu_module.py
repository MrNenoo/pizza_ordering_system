# menu_module.py

# === Pizza Base Menu ===
PIZZAS = {
    "Margherita": 200,
    "Pepperoni": 250,
    "Farmhouse": 220,
    "Tandoori Paneer": 240,
    "BBQ Chicken": 270,
    "Veggie Delight": 210
}

# === Size Options and Additional Prices ===
SIZES = {
    "Small": 0,
    "Medium": 50,
    "Large": 100
}

# === Crust Options and Additional Prices ===
CRUSTS = {
    "Thin": 0,
    "Cheese Burst": 60,
    "Stuffed": 80
}

# === Toppings and Prices ===
TOPPINGS = {
    "Extra Cheese": 30,
    "Mushrooms": 20,
    "Olives": 25,
    "Capsicum": 15,
    "Jalapenos": 25,
    "Onions": 15,
    "Paneer": 30,
    "Chicken Sausage": 35
}

def show_menu():
    """Prints the full pizza menu to the console."""
    print("\n🍕 Pizza Menu:")
    for name, price in PIZZAS.items():
        print(f"  {name:<20} ₹{price}")

    print("\n📏 Sizes (extra cost):")
    for size, add_price in SIZES.items():
        print(f"  {size:<10} +₹{add_price}")

    print("\n🍞 Crust Options (extra cost):")
    for crust, add_price in CRUSTS.items():
        print(f"  {crust:<15} +₹{add_price}")

    print("\n🧀 Toppings (each at extra cost):")
    for topping, add_price in TOPPINGS.items():
        print(f"  {topping:<20} +₹{add_price}")
    print()


def get_menu_data():
    """
    Returns all menu dictionaries so other modules can use them.

    :return: tuple of (pizzas, sizes, crusts, toppings)
    """
    return PIZZAS, SIZES, CRUSTS, TOPPINGS

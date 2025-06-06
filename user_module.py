import uuid
from menu_module import show_menu, get_menu_data
from validators import validate_name, validate_mobile, ValidationError
from order_module import Order

def take_order():
    print("\n🛒 Welcome to Pizza Order System!")
    show_menu()

    pizzas, sizes, crusts, toppings = get_menu_data()

    # Get user details
    while True:
        try:
            name = input("\nEnter your name: ")
            validate_name(name)
            break
        except ValidationError as ve:
            print(f"❌ {ve}")

    while True:
        try:
            mobile = input("Enter your mobile number: ")
            validate_mobile(mobile)
            break
        except ValidationError as ve:
            print(f"❌ {ve}")

    # Select base pizza
    while True:
        pizza_name = input("\nChoose your pizza: ").strip()
        if pizza_name in pizzas:
            base_price = pizzas[pizza_name]
            break
        else:
            print("❌ Invalid pizza. Try again.")

    # Select size
    while True:
        size = input("Choose size (Small/Medium/Large): ").capitalize()
        if size in sizes:
            size_price = sizes[size]
            break
        else:
            print("❌ Invalid size. Try again.")

    # Select crust
    while True:
        crust = input("Choose crust (Thin/Cheese Burst/Stuffed): ").title()
        if crust in crusts:
            crust_price = crusts[crust]
            break
        else:
            print("❌ Invalid crust. Try again.")

    # Select toppings (comma-separated)
    chosen_toppings = []
    topping_price_total = 0

    topping_input = input("Choose toppings (comma-separated): ")
    if topping_input.strip():
        for topping in map(str.strip, topping_input.split(",")):
            if topping in toppings:
                chosen_toppings.append(topping)
                topping_price_total += toppings[topping]
            else:
                print(f"⚠️ Skipped invalid topping: {topping}")

    # Final Price Calculation
    total_price = base_price + size_price + crust_price + topping_price_total

    # Create Order object (uuid for unique ID)
    order = Order(
        order_id=str(uuid.uuid4())[:8],
        customer_name=name,
        mobile_number=mobile,
        pizza=pizza_name,
        size=size,
        crust=crust,
        toppings=chosen_toppings,
        base_price=base_price,
        size_prices=size_price,
        crust_prices=crust_price,
        topping_prices=topping_price_total,
        total_price = total_price
    )

    print(f"\n🧾 Order Summary:\n{order}\n")
    return order

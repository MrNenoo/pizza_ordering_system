# admin_module.py

from menu_module import PIZZAS, SIZES, CRUSTS, TOPPINGS, show_menu
from data_module import load_orders_from_csv
from data_module import get_sales_summary
from analytics_module import show_sales_charts


def show_admin_menu():
    while True:
        print("\n🔐 Admin Panel:")
        print("1. View Menu")
        print("2. Add Pizza")
        print("3. Remove Pizza")
        print("4. Update Pizza Price")
        print("5. View All Orders")
        print("6. Show Sales Report")
        print("7. Show Sales Charts")
        print("8. Exit Admin Panel")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_menu()

        elif choice == "2":
            add_pizza_item()

        elif choice == "3":
            remove_pizza_item()

        elif choice == "4":
            update_pizza_price()

        elif choice == "5":
            view_all_orders()

        elif choice == "6":
            show_sales_report()

        elif choice == "7":
            show_sales_charts()

        elif choice == "8":
            print("✅ Exiting Admin Panel...")
            break

        else:
            print("❌ Invalid choice. Try again.")


def add_pizza_item():
    name = input("Enter new pizza name: ").strip()
    if name in PIZZAS:
        print("⚠️ Pizza already exists.")
        return
    try:
        price = int(input("Enter price: ").strip())
        PIZZAS[name] = price
        print(f"✅ {name} added at ₹{price}")
    except ValueError:
        print("❌ Invalid price entered.")


def remove_pizza_item():
    name = input("Enter pizza name to remove: ").strip()
    if name in PIZZAS:
        del PIZZAS[name]
        print(f"✅ {name} removed.")
    else:
        print("❌ Pizza not found.")


def update_pizza_price():
    name = input("Enter pizza name to update: ").strip()
    if name in PIZZAS:
        try:
            new_price = int(input("Enter new price: ").strip())
            PIZZAS[name] = new_price
            print(f"✅ {name} price updated to ₹{new_price}")
        except ValueError:
            print("❌ Invalid price.")
    else:
        print("❌ Pizza not found.")


def show_sales_report():
    summary = get_sales_summary()
    print("\n📊 Sales Summary")
    print(f"Total Orders: {summary['total_orders']}")
    print(f"Total Revenue: ₹{summary['revenue']:.2f}")
    print(f"Most Popular Pizza: {summary['most_popular']}")
    print("Orders by Size:")
    for size, count in summary["size_count"].items():
        print(f"  {size}: {count}")


def view_all_orders():
    orders = (load_orders_from_csv())
    if not orders:
        print("📭 No orders found.")
        return

    print("\n📋 Order History:")
    for order in orders:
        print(order)
        print("-" * 40)

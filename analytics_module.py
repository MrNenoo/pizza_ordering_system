import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
import csv
import os
matplotlib.use("TkAgg")

ORDER_FILE = "orders.csv"


def load_orders_from_csv():
    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, mode="r", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def show_sales_charts():
    toppings_counter = Counter()
    orders = load_orders_from_csv()
    if not orders:
        print("No orders available to display charts.")
        return

    pizza_counter = Counter()
    size_counter = Counter()
    revenue = 0

    for order in orders:
        pizza = order.get("pizza", "Unknown")
        size = order.get("size", "Unknown")
        price = order.get("price", "0")

        pizza_counter[pizza] += 1
        size_counter[size] += 1

        toppings_str = order.get("toppings", "")
        toppings = [t.strip() for t in toppings_str.split(",") if t.strip()]
        toppings_counter.update(toppings)

        try:
            revenue += float(price)
        except ValueError:
            continue

    print(f"\n📊 Total Revenue: ₹{revenue:.2f}")

    # 🍕 Most Popular Pizzas
    plt.figure(figsize=(8, 6))
    plt.bar(pizza_counter.keys(), pizza_counter.values(), color='tomato')
    plt.title("Most Popular Pizzas")
    plt.xlabel("Pizza")
    plt.ylabel("Orders")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 🧱 Size Distribution
    plt.figure(figsize=(6, 5))
    plt.pie(size_counter.values(), labels=size_counter.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Pizza Size Distribution")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

    # 🧀 Most Popular Toppings
    if toppings_counter:
        plt.figure(figsize=(8, 6))
        plt.bar(toppings_counter.keys(), toppings_counter.values(), color='mediumseagreen')
        plt.title("Most Popular Toppings")
        plt.xlabel("Topping")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

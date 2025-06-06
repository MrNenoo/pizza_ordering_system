# data_module.py

import csv
import os
from collections import Counter
from datetime import datetime

ORDER_FILE = "orders.csv"

FIELDNAMES = [
    "timestamp", "customer_name", "pizza", "size", "crust",
    "toppings", "price", "status"
]

def save_order_to_csv(order):
    """
    Save a single order dict to the CSV file.
    """
    is_new_file = not os.path.exists(ORDER_FILE)
    with open(ORDER_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if is_new_file:
            writer.writeheader()

        writer.writerow({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "customer_name": order.customer_name,
            "pizza": order.pizza,
            "size": order.size,
            "crust": order.crust,
            "toppings": ", ".join(order.toppings),
            "price": order.total_price,
            "status": order.status
        })


def load_orders_from_csv():
    """
    Load all orders from the CSV and return as list of dicts.
    """
    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_sales_summary():
    """
    Calculate and return:
    - Total revenue
    - Most popular pizza
    - Orders per size
    """
    orders = load_orders_from_csv()
    if not orders:
        return {
            "revenue": 0,
            "most_popular": None,
            "size_count": {},
            "total_orders": 0
        }

    total_revenue = 0
    pizza_counter = Counter()
    size_counter = Counter()

    for order in orders:
        try:
            total_revenue += float(order["price"])
        except ValueError:
            continue
        pizza_counter[order["pizza"]] += 1
        size_counter[order["size"]] += 1

    most_popular = pizza_counter.most_common(1)[0][0] if pizza_counter else None

    return {
        "revenue": total_revenue,
        "most_popular": most_popular,
        "size_count": dict(size_counter),
        "total_orders": len(orders)
    }

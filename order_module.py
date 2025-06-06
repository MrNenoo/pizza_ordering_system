import uuid
from datetime import datetime

class Order:
    def __init__(self, order_id, customer_name, mobile_number, pizza, base_price, size, crust, toppings, size_prices, crust_prices, topping_prices,total_price, status="Pending"):
        self.order_id = order_id
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.pizza = pizza
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.base_price = base_price
        self.size_prices = size_prices
        self.crust_prices = crust_prices
        self.topping_prices = topping_prices
        self.status = status
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total_price = total_price

    def calculate_price(self, size_prices, crust_prices, topping_prices):
        size_cost = size_prices
        crust_cost = crust_prices
        toppings_cost = topping_prices
        return self.total_price + size_cost + crust_cost + toppings_cost

    def update_status(self, new_status):
        self.status = new_status

    def summary(self):
        return {
            "Order ID": self.order_id,
            "User": self.customer_name,
            "Pizza": f"{self.pizza} ({self.size}, {self.crust})",
            "Toppings": self.toppings,
            "Total Price": self.total_price,
            "Status": self.status,
            "Time": self.timestamp
        }

    def __str__(self):
        return f"""
🧾 Order Summary:
---------------------
Order ID   : {self.order_id}
Customer   : {self.customer_name}
Pizza      : {self.pizza} ({self.size}, {self.crust})
Toppings   : {', '.join(self.toppings) if self.toppings else 'None'}
Total Price: ₹{self.total_price}
Status     : {self.status}
Time       : {self.timestamp}
"""

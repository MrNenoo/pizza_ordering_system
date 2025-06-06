import threading
import time

ORDER_STATUSES = [
    "Order Received",
    "Preparing Pizza",
    "Baking Pizza",
    "Out for Delivery",
    "Delivered"
]

def simulate_order_delivery(order, delay_per_stage=2):
    print(f"\n🕒 Starting delivery for Order ID: {order.order_id}")
    for status in ORDER_STATUSES:
        time.sleep(delay_per_stage)
        order.update_status(status)
        print(f"📦 Order ID {order.order_id} Status: {order.status}")
    print(f"✅ Order for {order.user_name} delivered!\n")

def simulate_multiple_orders(orders):
    threads = []
    for order in orders:
        t = threading.Thread(target=simulate_order_delivery, args=(order,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

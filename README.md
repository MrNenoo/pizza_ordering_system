# 🍕 Pizza Ordering System (Console-Based)

A modular Python application that simulates a complete pizza ordering experience with real-time order tracking, admin features, and sales analytics — all via the terminal.

---

## ✅ Features

**For Users:**
- Browse pizzas by category (Veg/Non-Veg)
- Customize size, crust, and toppings
- Dynamic pricing based on customizations
- Place orders with real-time status updates
- View past orders and track status

**For Admins:**
- Add, remove, update pizzas in the menu
- View all orders
- Analyze sales with reports and charts (most popular pizza/toppings, revenue)

---

## 🛠️ Key Concepts Covered

| Concept Area | Topics |
|--------------|--------|
| Core Python | Functions, Loops, Conditionals |
| Advanced Data Structures | Dictionaries, Lists, Sets |
| Functional Programming | Lambdas, map/filter |
| Object-Oriented Programming | Classes, Encapsulation, Inheritance |
| Modules and Packages | Modular code across multiple files |
| File I/O & Serialization | CSV-based order storage |
| Exception Handling | Input validation, graceful error messages |
| Iterators & Generators | Used in menu and order flow |
| Asynchronous Programming | Simulated real-time order tracking |
| Regular Expressions | Validating user inputs |
| External Libraries | `matplotlib` for sales visualization |
| Performance Concepts | Code profiling-ready, memory-conscious design |
| Version Control | Structured Git project with commits per feature |

---

## 📂 Project Structure

```
pizza_ordering_system/
├── main.py
├── menu_module.py
├── order_module.py
├── user_module.py
├── delivery_module.py
├── data_module.py
├── admin_module.py
├── analytics_module.py
├── orders.csv
└── README.md
```

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/MrNenoo/pizza_ordering_system.git
   cd pizza_ordering_system
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install matplotlib
   ```

4. **Run the app**
   ```bash
   python main.py
   ```

---

## 📈 Sample Analytics Output

- Bar chart: Most ordered pizzas
- Pie chart: Pizza size distribution
- Bar chart: Most selected toppings
- Total revenue printed in console

---

## 📊 Example Order Flow

```
Welcome to Python Pizza!
1. Browse Menu
2. Place Order
3. Track Order
4. Admin Login
```

---

## 👨‍💻 Author

- **Name:** MrNenoo  
- **GitHub:** [MrNenoo](https://github.com/MrNenoo)

---

## 📘 License

This project is licensed under the MIT License.

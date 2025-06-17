
from user_module import take_order
from admin_module import show_admin_menu
from data_module import save_order_to_csv

def main():
    print("🍕 Welcome to PyPizza Ordering System 🍕")

    while True:
        print("\nMain Menu:")
        print("1. Place an Order")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            order = take_order()
            if order:
                save_order_to_csv(order)
                print("✅ Order placed and saved successfully!")

        elif choice == "2":
            password = input("Enter Admin Password: ")
            if password == "admin123":
                show_admin_menu()
            else:
                print("❌ Incorrect password. Access denied.")

        elif choice == "3":
            print("👋 Thank you for using app. Goodbye!")
            break

        else:
            print("❌ Invalid input. Please try again.")

if __name__ == "__main__":
    main()

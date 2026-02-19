import json
import os

DATA_FILE = "hotel_data.json"

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def book_room(customers):
    print("\n--- Book a Room ---")
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    room_type = input("Room type (Single/Double/Deluxe): ").capitalize()
    days = int(input("Number of days: "))

    price_map = {
        "Single": 1000,
        "Double": 1800,
        "Deluxe": 3000
    }

    if room_type not in price_map:
        print("Invalid room type!")
        return

    total_bill = price_map[room_type] * days

    customer = {
        "name": name,
        "phone": phone,
        "room_type": room_type,
        "days": days,
        "bill": total_bill,
        "status": "Checked-in"
    }

    customers.append(customer)
    save_data(customers)

    print(f"\nRoom booked successfully! Total Bill: ₹{total_bill}")

def show_customers(customers):
    print("\n--- All Customers ---")
    if not customers:
        print("No records found.")
        return

    for i, c in enumerate(customers, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['room_type']} | {c['days']} days | ₹{c['bill']} | {c['status']}")

def checkout(customers):
    print("\n--- Check-out ---")
    phone = input("Enter phone number to checkout: ")

    for c in customers:
        if c["phone"] == phone and c["status"] == "Checked-in":
            c["status"] = "Checked-out"
            save_data(customers)
            print(f"Checkout successful. Total bill: ₹{c['bill']}")
            return

    print("Customer not found or already checked out.")

def main():
    customers = load_data()

    while True:
        print("\n====== HOTEL MANAGEMENT SYSTEM ======")
        print("1. Book Room")
        print("2. Show All Customers")
        print("3. Check-out")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_room(customers)
        elif choice == "2":
            show_customers(customers)
        elif choice == "3":
            checkout(customers)
        elif choice == "4":
            print("Thank you! Exiting system...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
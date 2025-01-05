# inventory list
inventory = []

def add_item(name, price, quantity, category):
    #Adds a new item to the inventory
    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    inventory.append(item)
    print(f"Item {name} added successfully")

def remove_item(name):
    #Removes an item from the inventory by name
    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"Item {name} removed successfully")
            return
    print(f"Item {name} not found in the inventory")

def update_item(name, price=None, quantity=None):
    # updates the price or quantity of an existing item
    for item in inventory:
        if item['name'].lower() == name.lower():
            if price is not None:
                item['price'] = price
            if quantity is not None:
                item['quantity'] = quantity
            print(f"Item {name} updated successfully")
            return
    print(f"Item {name} not found in inventory")

def search_by_category(category):
    #Seaches and display all items in a specific category
    print(f"Items in category {category} :")
    found_items = [item for item in inventory if item['category'].lower() == category.lower()]
    if found_items:
        for item in found_items:
            print(f"- {item['name']}: Price:${item['price']}, Quantity:{item['quantity']}")
    else:
        print(f"No items found in category {category}")

def display_inventory():
    #Displays the current inventory
    if not inventory:
        print(f"No items in inventory")
        return
    print(f"Current Market Inventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}, Category: {item['category']}"
        )

def main():
    while True:
        print("\nMarket Inventory Management")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. Search by Category")
        print("5. Display Inventory")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                category = input("Enter item category: ")
                add_item(name, price, quantity, category)
            except ValueError:
                print("Invalid input for price or quantity. Please try again.")

        elif choice == "2":
            name = input("Enter the name of the item to remove: ")
            remove_item(name)
        elif choice == "3":
            name = input("Enter the name of the item to update: ")
            try:
                price = input("Enter new price (or press Enter to skip): ")
                price = float(price) if price else None
                quantity = input("Enter new quantity (or press Enter to skip): ")
                quantity = int(quantity) if quantity else None
                update_item(name, price, quantity)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "4":
            category = input("Enter the category to search: ")
            search_by_category(category)
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            print("Exiting the program")
            break
        else:
            print(f"Invalid chose. Please enter a number between 1 and 6")

if __name__ == "__main__":
   main()

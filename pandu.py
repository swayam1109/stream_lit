class Item:
    def __init__(self, item_id, name, category, image):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.image = image

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Category: {self.category}"

def display_items(items):
    for item in items:
        print(item)

def select_item(items):
    while True:
        try:
            selected_id = int(input("Enter the ID of the item you want to try on (0 to exit): "))
            if selected_id == 0:
                break
            item = next((item for item in items if item.item_id == selected_id), None)
            if item:
                print(f"\nYou selected: {item.name}")
                print(f"Visualizing {item.name}...\n")
                print(item.image)  # Display the image as text (simulated)
            else:
                print("Invalid ID. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    clothing_items = [
        Item(1, "T-Shirt", "Clothing", "🧥 T-Shirt Image Placeholder"),
        Item(2, "Jeans", "Clothing", "👖 Jeans Image Placeholder"),
        Item(3, "Dress", "Clothing", "👗 Dress Image Placeholder"),
    ]

    furniture_items = [
        Item(4, "Chair", "Furniture", "🪑 Chair Image Placeholder"),
        Item(5, "Table", "Furniture", "🛋 Table Image Placeholder"),
        Item(6, "Sofa", "Furniture", "🛋 Sofa Image Placeholder"),
    ]

    while True:
        print("\nWelcome to the Virtual Shopping App!")
        print("1. View Clothing Items")
        print("2. View Furniture Items")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("\nClothing Items:")
            display_items(clothing_items)
            select_item(clothing_items)
        elif choice == "2":
            print("\nFurniture Items:")
            display_items(furniture_items)
            select_item(furniture_items)
        elif choice == "3":
            print("Thank you for visiting the Virtual Shopping App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

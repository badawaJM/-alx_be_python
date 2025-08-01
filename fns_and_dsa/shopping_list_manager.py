def display_menu():
    print("\n=== Shopping List Manager ===")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Show the list")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter the name of the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your list.")
            else:
                print("Empty item name. Please try again.")

        elif choice == '2':
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your list.")
            else:
                print(f"'{item}' is not in the list.")

        elif choice == '3':
            if shopping_list:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): ").strip())

            if choice == 1:  # Add an item
                item = input("Enter the item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f'"{item}" has been added to the shopping list.')
                else:
                    print("Item name cannot be empty.")

            elif choice == 2:  # Remove an item
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f'"{item}" has been removed from the shopping list.')
                else:
                    print(f'"{item}" is not in the shopping list.')

            elif choice == 3:  # View the shopping list
                if shopping_list:
                    print("\nYour shopping list:")
                    for i, item in enumerate(shopping_list, start=1):
                        print(f"{i}. {item}")
                else:
                    print("Your shopping list is empty.")

            elif choice == 4:  # Exit the program
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    def add(item):
      shopping_list.append(item)

    def display():
      print(shopping_list)

    def delete(item):
      shopping_list.remove(item)
    
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
          item = input("item? ")
          add(item)
          pass
        elif choice == '2':
            item = input("item? ")
            delete(item)
    
        elif choice == '3':
             display()
             pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
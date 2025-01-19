shopping_list = []
item = " "
m = 0
lef = len(shopping_list)

def menu_display():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add(item):
    shopping_list.append(item)

def display():
    print(shopping_list)

def delete(item):
   shopping_list.remove(item)

while m < 10:
     menu_display()
     menu = input("Enter your choice: ")
     match menu:
        case "1":
           item = input("item? ")
           add(item)
        case "3":
          display()
        case "2":
             item = input("item? ")
             delete(item)
        case "4":
          print("Goodbye!")
          break
        case _:
             print(f"Invalid choice. Please try again.")
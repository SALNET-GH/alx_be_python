number = int(input("Enter a number to see its multiplication table: "))

for j in range(1, 10):
    result = (number * j) 
    print(f"{number} * {j} = {result}")
    j += 1
    print()
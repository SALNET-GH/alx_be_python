number = int(input("Enter a number to see its multiplication table: "))
j = 0
for j in range(1, 11):
    (result) = (number * (j)) 
    print(f"{number} * {j} = {result}")
    j += 1
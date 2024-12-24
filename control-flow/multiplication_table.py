number = int(input("Enter a number to see its multiplication table: "))

times = [1,2,3,4,5,6,7,8,9,10]
for j in times:
    result = (number * j) 
    print(f"{number} * {j} = {result}")
    j += 1
    print()
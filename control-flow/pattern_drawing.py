pattern_length = int(input("Enter the size of the pattern: "))
l = pattern_length

while l == pattern_length:
    for l in range(0, pattern_length):
        for j in range(0, pattern_length):
          print("*", end="")
        print()
l += 1

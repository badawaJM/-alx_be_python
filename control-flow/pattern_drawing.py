size_of_pattern = int(input("Enter the size of the pattern:"))
line = 0
while line < size_of_pattern:
    for column in range (0, size_of_pattern):
        print("*", end="")
    print()
    line += 1 
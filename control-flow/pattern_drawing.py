size = int(input("Enter the size of the pattern:"))
i = 1
while i <= size:
    for x in range(size):
        print("*", end="")
    print()
    i += 1
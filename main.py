rows = int(input("Enter Number of rows : "))

for i in range (rows):
    for j in range(i+1):
        print("*", end="")
    print()

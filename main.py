rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if j <= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

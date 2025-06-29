<<<<<<< HEAD
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
=======
# This is used to create a triangle with * pattern


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if j <= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next line after each row
>>>>>>> df65c41b6269023bb1500aa92dd4cbce7eff2ba3

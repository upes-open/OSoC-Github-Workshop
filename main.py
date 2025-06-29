rows = int(input("Enter the number of rows: "))
print("THIS IS A RIGHT ANGLE TRIANGLE PATTERN")
for i in range(1,rows+1):
    for j in range(1, i+1):
        print("*", end="")
    print()

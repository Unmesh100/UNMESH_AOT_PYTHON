# Taking user input for the number of rows
rows = int(input("Enter the number of rows for the full pyramid: "))

# Loop to print the upper half of the full pyramid (including the middle row)
for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()  # Newline after each row

# Loop to print the lower half of the full pyramid
for i in range(rows - 1, 0, -1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    
    # Print decreasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()  # Newline after each row

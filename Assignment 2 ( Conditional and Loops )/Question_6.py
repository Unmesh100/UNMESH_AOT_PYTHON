# Taking user input for the number of rows
rows = int(input("Enter the number of rows for the inverted pyramid: "))

# Loop through each row, starting from the given number of rows down to 1
for i in range(rows, 0, -1):
    # Print spaces for the pyramid shape
    print(" " * (rows - i), end="")
    
    # Print stars for each row
    print("* " * i)

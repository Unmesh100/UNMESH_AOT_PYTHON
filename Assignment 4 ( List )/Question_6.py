# Input for the list of numbers
numbers = input("Enter numbers separated by spaces: ").split()
# Convert input strings to integers
numbers = [int(num) for num in numbers]

# Create lists to hold unique elements and duplicates
unique_numbers = []
duplicates = []

# Loop through the original list
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
    else:
        duplicates.append(num)

# Combine unique numbers with duplicates
result = unique_numbers + duplicates

# Print the result
print("The list after moving duplicates to the end is:", result)

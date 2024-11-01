# Input for the list of numbers
numbers = input("Enter elements of the list separated by spaces: ").split()
# The list now contains strings, so we convert them to integers if needed
# numbers = [int(num) for num in numbers]  # Uncomment if you want integers

# Get the length of the list
n = len(numbers)

# Loop to swap elements
for i in range(n // 2):
    # Swap the ith element with the (n-i-1)th element
    numbers[i], numbers[n - i - 1] = numbers[n - i - 1], numbers[i]

# Print the reversed list
print("Reversed list:", numbers)


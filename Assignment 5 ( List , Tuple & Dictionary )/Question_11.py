# Taking input for the numbers from the user
# User can input numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Splitting the input string into a list of numbers (as strings)
numbers = user_input.split()

# Initializing the sum variable
positive_sum = 0

# Looping through the list of numbers
for num in numbers:
    try:
        # Convert the string to a float (or int)
        value = float(num)  # Using float to handle both integers and decimals
        # Check if the value is positive
        if value > 0:
            positive_sum += value  # Add to the sum if it's positive
    except ValueError:
        print(f"'{num}' is not a valid number and will be ignored.")

# Display the sum of positive values
print("Sum of positive values:", positive_sum)

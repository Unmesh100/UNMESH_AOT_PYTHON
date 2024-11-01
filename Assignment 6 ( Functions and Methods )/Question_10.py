def format_number(number):
    # Convert the number to a string with commas as thousand separators
    return f"{number:,}"

# Taking user input
try:
    # Prompt user to enter a non-negative integer
    number = int(input("Enter a non-negative number: "))
    
    # Check if the number is non-negative
    if number < 0:
        print("Please enter a non-negative number.")
    else:
        # Format and print the number
        formatted_number = format_number(number)
        print("Formatted number with commas:", formatted_number)
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")

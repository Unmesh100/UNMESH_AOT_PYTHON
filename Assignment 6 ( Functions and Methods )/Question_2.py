def get_consecutive_integers(start):
    # Generate a list of 10 consecutive integers starting from 'start'
    return [start + i for i in range(10)]

# Get user input
user_input = input("Enter an integer: ")

# Check if the input is a valid integer
if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    user_input = int(user_input)  # Convert to integer
    consecutive_integers = get_consecutive_integers(user_input)
    print("The list of ten consecutive integers is:", consecutive_integers)
else:
    print("Please enter a valid integer.")

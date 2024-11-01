# Taking user input for the number to check
number = int(input("Enter a number to check if it is a magic number: "))

# Store the original number for later comparison
original_number = number

# Loop to calculate the repeated sum of digits until a single digit is reached
while number > 9:
    digit_sum = 0

    # Add up the digits of the current number
    while number > 0:
        digit_sum += number % 10
        number //= 10

    # Update the number with the sum of its digits
    number = digit_sum

# Check if the final single digit is 1
if number == 1:
    print(original_number, "is a magic number.")
else:
    print(original_number, "is not a magic number.")

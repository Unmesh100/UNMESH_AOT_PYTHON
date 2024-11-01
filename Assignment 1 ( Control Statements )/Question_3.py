# Number Reversal and Parity Checker

# Program Introduction
print("Number Reversal Program:")
print("------------------------")

# Input number
while True:
    # Get input from user
    number = input("Enter a 2-digit or 3-digit number: ")
    
    # Validate input
    if number.isdigit() and (len(number) == 2 or len(number) == 3):
        # Convert input to integer
        number = int(number)
        break
    else:
        print("Please enter a valid 2-digit or 3-digit number!")

# 2-digit number reversal
if 10 <= number <= 99:
    # Reverse 2-digit number
    reversed_number = (number % 10) * 10 + (number // 10)
    
    # Check even or odd
    if number % 2 == 0:
        number_type = "Even"
    else:
        number_type = "Odd"
    
    # Print results
    print("\n2-Digit Number Results:")
    print(f"Original Number: {number}")
    print(f"Reversed Number: {reversed_number}")
    print(f"Number Type: {number_type}")

# 3-digit number reversal
elif 100 <= number <= 999:
    # Reverse 3-digit number
    hundreds = number // 100
    tens = (number % 100) // 10
    ones = number % 10
    
    reversed_number = ones * 100 + tens * 10 + hundreds
    
    # Check even or odd
    if number % 2 == 0:
        number_type = "Even"
    else:
        number_type = "Odd"
    
    # Additional analysis
    print("\n3-Digit Number Results:")
    print(f"Original Number: {number}")
    print(f"Reversed Number: {reversed_number}")
    print(f"Number Type: {number_type}")
    print(f"Hundreds Digit: {hundreds}")
    print(f"Tens Digit: {tens}")
    print(f"Ones Digit: {ones}")
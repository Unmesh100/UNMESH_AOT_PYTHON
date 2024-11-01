# Print the program introduction
print("Square Root Primality Checker")
print("-----------------------------")

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Calculate the square root of the number
sqrt = num ** 0.5

# Check if the square root is an integer
if sqrt.is_integer():
    # If the square root is an integer, check if it's a prime number
    is_prime = True
    for i in range(2, int(sqrt) + 1):
        if int(sqrt) % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"The square root of {num} is {int(sqrt)}, which is a prime number.")
    else:
        print(f"The square root of {num} is {int(sqrt)}, which is not a prime number.")
else:
    print(f"The square root of {num} is not an integer.")
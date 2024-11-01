# Without Recursion
number = int(input("Enter a number to find its factorial: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i  # Multiply each i with factorial

    print("Factorial of", number, "is", factorial)

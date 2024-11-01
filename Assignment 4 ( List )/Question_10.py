import math

# Input for the list of numbers
numbers = input("Enter numbers separated by spaces: ").split()
# Convert input strings to floats
numbers = [float(num) for num in numbers]

# Calculate the arithmetic mean
mean = sum(numbers) / len(numbers)

# Calculate the variance
variance = sum((num - mean) ** 2 for num in numbers) / len(numbers)

# Calculate the standard deviation
std_deviation = math.sqrt(variance)

# Print the results
print(f"Arithmetic Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")

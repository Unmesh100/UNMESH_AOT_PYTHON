# Input for the list of numbers
numbers = input("Enter numbers separated by spaces: ").split()
# Convert input strings to integers
numbers = [int(num) for num in numbers]

# Input for the range of indices
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

# Validate indices
if start_index < 0 or end_index >= len(numbers) or start_index > end_index:
    print("Invalid indices. Please ensure they are within the list range and start index is less than or equal to end index.")
else:
    # Extract the sublist
    sublist = numbers[start_index:end_index + 1]

    # Calculate the maximum and minimum values
    max_value = max(sublist)
    min_value = min(sublist)

    # Print the results
    print(f"The maximum value in the specified range is: {max_value}")
    print(f"The minimum value in the specified range is: {min_value}")

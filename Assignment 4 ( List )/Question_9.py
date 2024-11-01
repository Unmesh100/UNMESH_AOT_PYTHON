# Function to search for a number in a list
def search_number_in_list(number_list, target):
    # Iterate through the list
    for index in range(len(number_list)):
        # Check if the current element is the target
        if number_list[index] == target:
            return index  # Return the index if found
    return -1  # Return -1 if the number is not found

# Input for the list of numbers
numbers = input("Enter numbers separated by spaces: ").split()
# Convert input strings to integers
numbers = [int(num) for num in numbers]

# Input for the number to search
target_number = int(input("Enter the number to search: "))

# Call the function and store the result
result_index = search_number_in_list(numbers, target_number)

# Output the result
if result_index != -1:
    print(f"The number {target_number} is found at index: {result_index}")
else:
    print(f"The number {target_number} is not found in the list.")

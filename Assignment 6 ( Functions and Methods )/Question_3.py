def find_max_min_with_indices():
    # Get user input as a list of integers
    user_input = input("Enter a list of integers separated by spaces: ")
    
    # Convert input string to a list of integers
    int_list = [int(num) for num in user_input.split()]
    
    if not int_list:
        return "The list is empty."

    # Find the maximum and minimum values and their indices
    max_value = max(int_list)
    min_value = min(int_list)
    max_indices = [i for i, value in enumerate(int_list) if value == max_value]
    min_indices = [i for i, value in enumerate(int_list) if value == min_value]

    return {
        'max_value': max_value,
        'max_indices': max_indices,
        'min_value': min_value,
        'min_indices': min_indices
    }

# Call the function and display the result
result = find_max_min_with_indices()
print(result)

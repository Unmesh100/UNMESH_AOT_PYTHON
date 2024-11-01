# Function to return a list of unique elements
def unique_elements(input_list):
    unique_list = []  # Initialize an empty list to store unique elements
    for item in input_list:
        if item not in unique_list:  # Check if the item is not already in the unique_list
            unique_list.append(item)  # Add the item to the unique_list if it's not a duplicate
    return unique_list  # Return the list of unique elements

# Input for the original list
sample_list = input("Enter elements of the list separated by spaces: ").split()
# Convert input strings to integers
sample_list = [int(num) for num in sample_list]

# Call the function to get the unique elements
result = unique_elements(sample_list)

# Print the unique list
print("Unique List:", result)

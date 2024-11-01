# Taking input for keys and values from the user
keys_input = input("Enter keys separated by commas: ")
values_input = input("Enter values separated by commas: ")

# Splitting the input strings into lists
keys = keys_input.split(',')
values = values_input.split(',')

# Converting values to integers
values = [int(value.strip()) for value in values]  # Convert each value to an integer

# Creating a dictionary using zip
dictionary = dict(zip(keys, values))

# Displaying the resulting dictionary
print("Created Dictionary:", dictionary)

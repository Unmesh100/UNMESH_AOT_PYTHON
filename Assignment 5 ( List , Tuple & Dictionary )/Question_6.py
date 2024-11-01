# Taking input for the first dictionary
print("Enter the first dictionary (key:value pairs separated by commas):")
dict1_input = input()
dict1 = dict(item.split(':') for item in dict1_input.split(','))

# Taking input for the second dictionary
print("Enter the second dictionary (key:value pairs separated by commas):")
dict2_input = input()
dict2 = dict(item.split(':') for item in dict2_input.split(','))

# Merging the two dictionaries
merged_dict = dict1.copy()  # Create a copy of dict1 to avoid modifying the original
merged_dict.update(dict2)  # Merge dict2 into the copy of dict1

# Displaying the merged dictionary
print("Merged Dictionary:", merged_dict)

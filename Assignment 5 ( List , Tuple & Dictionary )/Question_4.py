# Original tuple
tuple1 = (11, [22], 33, 44, 55)

# Display the original tuple
print("Original Tuple:", tuple1)

# Taking user input to modify the first item of the list
new_value = input("Enter the new value to replace 22: ")

# Modify the first item (index 0) of the list inside the tuple
tuple1[1][0] = new_value  # Accessing the list and changing the first element

# Display the modified tuple
print("Modified Tuple:", tuple1)

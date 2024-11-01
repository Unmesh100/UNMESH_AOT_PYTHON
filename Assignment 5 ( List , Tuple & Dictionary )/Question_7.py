# Take dictionary input from user as a string
dict_input = input("Enter a dictionary (e.g., {'a': 100, 'b': 200, 'c': 300}): ")

# Convert string to dictionary
sampleDict = eval(dict_input)

# Take value input from user
value = int(input("Enter the value to check: "))

# Check if the value exists in the dictionary
if value in sampleDict.values():
    print(f"The value {value} exists in the dictionary.")
else:
    print(f"The value {value} does not exist in the dictionary.")

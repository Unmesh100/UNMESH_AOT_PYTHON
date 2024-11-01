# Given data set
data_set = [{'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}]

# Access and print values
print("Original Data Set:")
print(data_set)

# Accessing values by keys
print("\nValue for 'a':", data_set[0]['a'])
print("Value for 'b':", data_set[0]['b'])

# Modifying the value for key 'c'
data_set[0]['c'] = 'THREE'
print("\nModified value for 'c':", data_set)

# Adding a new key-value pair
data_set[0]['g'] = 'seven'
print("\nData Set after adding key 'g':", data_set)

# If you want to get all keys and values
print("\nAll keys and values in the dictionary:")
for key, value in data_set[0].items():
    print(f"{key}: {value}")

# Input for the list of strings
str_list = input("Enter strings separated by spaces: ").split()

# Initialize variables to keep track of the longest string
longest_string = ""
longest_length = 0

# Loop through the list to find the longest string
for s in str_list:
    if len(s) > longest_length:
        longest_length = len(s)
        longest_string = s

# Print the longest string and its length
print("The longest string is:", longest_string)
print("The length of the longest string is:", longest_length)

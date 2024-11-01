s = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0

for char in s:
    if char.isupper():       # Check if the character is uppercase
        uppercase_count += 1
    elif char.islower():      # Check if the character is lowercase
        lowercase_count += 1

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)


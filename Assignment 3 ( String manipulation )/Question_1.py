s = input("Enter the string: ")
result = []

for char in s:
    # Check if last character in result matches current character
    if result and result[-1] == char:
        result.pop()  # Remove the last character (pair found)
    else:
        result.append(char)  # Add current character to result

# Check if result is empty
if not result:
    print("Empty String")
else:
    print("".join(result))

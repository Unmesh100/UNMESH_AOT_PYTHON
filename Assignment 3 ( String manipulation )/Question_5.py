s = input("Enter a string: ")
count = [0] * 26  # Array to store counts of each letter from 'a' to 'z'

# Count each character in the string
for char in s:
    index = ord(char) - ord('a')  # Calculate the index of the character
    count[index] += 1

# Check if each character's count matches its ASCII value in Byteland
is_super_ascii = True
for i in range(26):
    if count[i] != 0:  # Only check letters that appear in the string
        if count[i] != i + 1:  # ASCII value of 'a' in Byteland is 1, 'b' is 2, etc.
            is_super_ascii = False
            break

# Print the result
if is_super_ascii:
    print("Yes")
else:
    print("No")

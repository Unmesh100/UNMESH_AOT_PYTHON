s = input("Enter a string: ").lower()  # Convert input to lowercase
alphabet = set("abcdefghijklmnopqrstuvwxyz")
found_letters = set()

for char in s:
    if char in alphabet:  # Check if the character is a letter
        found_letters.add(char)

# Check if we found all letters
if found_letters == alphabet:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")


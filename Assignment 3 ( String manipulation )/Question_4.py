s = input("Enter a string: ").lower()  # Convert input to lowercase
reversed_s = s[::-1]  # Reverse the string

# Check if the original string is the same as the reversed string
if s == reversed_s:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


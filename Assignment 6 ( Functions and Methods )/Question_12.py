def is_palindrome(S):
    # Convert the string to lowercase to handle case insensitivity
    S = S.lower()
    # Compare the string with its reverse
    return S == S[::-1]

# Taking user input
S = input("Enter a string: ")
if is_palindrome(S):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

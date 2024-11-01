print("Enter numbers (type 'q' to quit):")

# Empty list to store palindrome numbers
palindromes = []

while True:
    user_input = input("Enter a number: ")
    
    # Check if the input is 'q' to quit the loop
    if user_input == 'q' :
        break
    
    if user_input == 'Q' :
        break

    # Check if input is a number
    if user_input.isdigit():
        number = int(user_input)
        
        # Convert number to a string and check if it reads the same forward and backward
        if str(number) == str(number)[::-1]:
            palindromes.append(number)

# Print the list of palindrome numbers
print("Palindrome numbers entered:", palindromes)

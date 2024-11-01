# Initialize an empty list
letter_list = []

# Loop through numbers 1 to 26
for i in range(1, 27):
    # Get the corresponding letter using chr
    letter = chr(96 + i)  # 'a' is 97 in ASCII, so we add 96 to i
    # Append the letter repeated i times
    letter_list.append(letter * i)

# Print the result
print(letter_list)


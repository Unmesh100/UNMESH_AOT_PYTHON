message = input("Enter your PlainText: ")
key = int(input("Enter the Key: "))

# Validate the key
if key < 1 or key > 25:
    print("INVALID INPUT")
else:
    encrypted_text = ""

    for char in message:
        # Shift uppercase letters
        if 'A' <= char <= 'Z':
            new_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            encrypted_text += new_char
        # Shift lowercase letters
        elif 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            encrypted_text += new_char
        # Shift digits
        elif '0' <= char <= '9':
            new_char = chr(((ord(char) - ord('0') + key) % 10) + ord('0'))
            encrypted_text += new_char
        # Leave other characters unchanged
        else:
            encrypted_text += char

    # Print the encrypted message
    print("The encrypted Text is:", encrypted_text)


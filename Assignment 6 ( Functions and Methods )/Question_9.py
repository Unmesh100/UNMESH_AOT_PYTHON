def CustomCaesarCipher(key, message):
    # Check if key is within valid range
    if key < 1 or key > 25:
        return "INVALID INPUT"
    
    encrypted_message = ""
    
    for char in message:
        # Shift uppercase letters
        if 'A' <= char <= 'Z':
            shifted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            encrypted_message += shifted_char
        # Shift lowercase letters
        elif 'a' <= char <= 'z':
            shifted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            encrypted_message += shifted_char
        # Shift digits
        elif '0' <= char <= '9':
            shifted_char = chr((ord(char) - ord('0') + key) % 10 + ord('0'))
            encrypted_message += shifted_char
        # Non-alphanumeric characters remain unchanged
        else:
            encrypted_message += char
            
    return encrypted_message

# Example usage:
try:
    message = input("Enter your PlainText: ")
    key = int(input("Enter the Key: "))
    encrypted_text = CustomCaesarCipher(key, message)
    print("The encrypted Text is:", encrypted_text)
except ValueError:
    print("INVALID INPUT")

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    # Adjust shift for decryption
    if not encrypt:
        shift = -shift
    
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, don't change it
            result += char
    
    return result

def main():
    # Get user input for the operation
    choice = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' or 'D'.")
        return
    
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Determine whether to encrypt or decrypt
    if choice == 'E':
        encrypted_text = caesar_cipher(text, shift, encrypt=True)
        print(f"Encrypted message: {encrypted_text}")
    else:
        decrypted_text = caesar_cipher(text, shift, encrypt=False)
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()

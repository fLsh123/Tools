from PIL import Image

def encrypt_decrypt_image(input_image_path, output_image_path, key):
    # Open an image file
    with Image.open(input_image_path) as img:
        # Convert image to RGB mode if not already in that mode
        img = img.convert("RGB")
        
        # Get image dimensions
        width, height = img.size
        
        # Create a new image object to store the encrypted/decrypted image
        encrypted_img = Image.new("RGB", (width, height))
        
        # Process each pixel
        for x in range(width):
            for y in range(height):
                # Get the pixel value at (x, y)
                r, g, b = img.getpixel((x, y))
                
                # Encrypt/Decrypt the pixel by XORing each channel with the key
                encrypted_r = r ^ key
                encrypted_g = g ^ key
                encrypted_b = b ^ key
                
                # Set the encrypted/decrypted pixel in the new image
                encrypted_img.putpixel((x, y), (encrypted_r, encrypted_g, encrypted_b))
        
        # Save the encrypted/decrypted image
        encrypted_img.save(output_image_path)
        print(f"Image saved as {output_image_path}")

def main():
    # Get user input for operation
    operation = input("Do you want to encrypt or decrypt the image? (E/D): ").upper()
    if operation not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' for encrypt or 'D' for decrypt.")
        return
    
    # Get image paths and encryption key
    input_image_path = input("Enter the path of the image: ")
    output_image_path = input("Enter the path to save the processed image: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))
    
    # Perform encryption or decryption
    encrypt_decrypt_image(input_image_path, output_image_path, key)
    print("Operation completed.")

if __name__ == "__main__":
    main()

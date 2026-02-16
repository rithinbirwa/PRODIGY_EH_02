from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Apply encryption formula
            r_enc = (r + key) % 256
            g_enc = (g + key) % 256
            b_enc = (b + key) % 256

            pixels[x, y] = (r_enc, g_enc, b_enc)

    img.save(output_image)
    print("Encryption completed.")


def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Reverse encryption formula
            r_dec = (r - key) % 256
            g_dec = (g - key) % 256
            b_dec = (b - key) % 256

            pixels[x, y] = (r_dec, g_dec, b_dec)

    img.save(output_image)
    print("Decryption completed.")


# ---- User Input ----
choice = input("Enter 1 for Encrypt, 2 for Decrypt: ")
key = int(input("Enter encryption key (0-255): "))

if choice == "1":
    encrypt_image("input.jpg", "encrypted.jpg", key)
elif choice == "2":
    decrypt_image("encrypted.jpg", "decrypted.jpg", key)
else:
    print("Invalid choice")

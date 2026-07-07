# Encrypt and decrypt a text file using simple character shifting.

# Get file name.
file_name = input("Enter file name: ")

# Read file content.
with open(file_name, "r") as file:
    text = file.read()


# Encrypt text.
encrypted_text = ""

for character in text:
    encrypted_text += chr(ord(character) + 3)


# Save encrypted file.
with open("encrypted.txt", "w") as file:
    file.write(encrypted_text)

print("File encrypted successfully.")
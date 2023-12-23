print('**** CAESARS CIPHER ****')

# Asking whether the user wants to encrypt or decrypt
user_choice = input('To Encrypt enter (e) / To decrypt enter (d): ')

# The key
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

def encrypt(message, shift):
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('Encrypted text:', encrypted_text)

def decrypt(encrypted_message, shift):
    decrypted_text = ''
    for char in encrypted_message:
        if char == ' ':
            decrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
    print('Decrypted text:', decrypted_text)

# Depending on user choice, perform encryption or decryption
if user_choice.lower() == 'e':
    # This is the word to be encrypted
    message = input('Enter the words to encrypt: ')
    # This is by how much we want to shift the letters across the alphabet key
    shift = int(input('Enter your desired shift on the alphabet: '))
    encrypt(message, shift)
elif user_choice.lower() == 'd':
    # This is the word to be decrypted
    encrypted_text = input('Enter the words to decrypt: ')
    # This is by how much we want to shift the letters across the alphabet key
    shift = int(input('Enter your desired shift on the alphabet: '))
    decrypt(encrypted_text, shift)
else:
    print('Invalid input. To Encrypt enter (e) / To decrypt enter (d)')

print('**** CAESARS CIPHER ****')
# this is the word to be encrypted
message = input('Enter the words to encrypt: ')
# this is by how much we want to shift the letters across the alphabet key
shift = int(input('Enter your desired shift on the alphabet: '))
# the key
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'


# encrypted_text = ''
def encrypt(message, shift):
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            # print(index)
            new_index = (int(index) + int(shift)) % len(alphabet)
            # print(new_index)
            encrypted_text += alphabet[new_index]
    print(encrypted_text)

encrypt(message, shift)

encrypted_text = encrypt(message, shift)
# this is the decryption function
def decrypt(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        if char == ' ':
            decrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
    print('Decrypted text:', decrypted_text)

# Call the decrypt function
decrypt(encrypted_text, shift)

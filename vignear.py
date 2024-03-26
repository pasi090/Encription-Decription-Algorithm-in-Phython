import string

def vigenere_cipher(text, key, encrypt=True):
    # Create a repeated key matching the length of the text
    repeated_key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]

    result = []
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            # Determine the shift based on the key
            shift = ord(repeated_key[i].lower()) - ord('a')
            if not encrypt:
                shift = -shift

            # Apply the shift to the character
            if char.isupper():
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            # Preserve non-alphabetic characters
            result.append(char)

    return ''.join(result)
def main():
    # User inputs
    text = input('Enter the text which you want to ENC/DEC using  vigenere_cipher: \n')
    key = input('Enter the keyword for ENC/DEC process: \n').lower()
    encrypt = input('Enter encrypt to ENCRYPT, decrypt to DECRYPT: \n').lower() == 'encrypt'

    # Perform Vigenère cipher operation
    result = vigenere_cipher(text, key, encrypt)

    # Display the result
    print('Result:', result)

if __name__ == "__main__":
    main()

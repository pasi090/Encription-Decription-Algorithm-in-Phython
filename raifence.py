def railfence_cipher_encrypt(text, key,encrypt):
    if key <= 1:
        return "Key must be greater than 1 for Rail Fence Cipher."

    # Create an empty matrix to represent the rail fence
    matrix = [[' ' for _ in range(len(text))] for _ in range(key)]

    row, direction = 0, 1  # Initialize starting row and direction

    # Fill the matrix with characters from the text
    for i in range(len(text)):
        matrix[row][i] = text[i]

        # Move to the next row based on the direction
        row += direction

        # Change direction if at the top or bottom rail
        if row == 0 or row == key - 1:
            direction *= -1

    # Read the matrix to retrieve the ciphered text
    result = []
    for i in range(key):
        result.extend(matrix[i])

    return ''.join(result)

def railfence_cipher_decrypt(ciphertext, key, decrypt):
    if key <= 1:
        return "Key must be greater than 1 for Rail Fence Cipher."

    # Create an empty matrix to represent the rail fence
    matrix = [[' ' for _ in range(len(ciphertext))] for _ in range(key)]

    row, direction = 0, 1  # Initialize starting row and direction

    # Fill the matrix with placeholders
    for i in range(len(ciphertext)):
        matrix[row][i] = 'X'
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    # Fill the matrix with ciphertext
    char_index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if matrix[i][j] == 'X' and char_index < len(ciphertext):
                matrix[i][j] = ciphertext[char_index]
                char_index += 1

    # Read the matrix to retrieve the decrypted text
    result = []
    row, direction = 0, 1
    for i in range(len(ciphertext)):
        result.append(matrix[row][i])
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    return ''.join(result).replace('X', '')




    
def main():
    # User inputs
    print('==========================================================\n')
    print('                ENCRYPT YOUR PLAIN_TEXT\n                 \n')
    print('==========================================================\n')

    text = input('Enter the text: \n')
    key = int(input('Enter the key: \n'))
    encrypt = input('Press E to encrypt your Plaintext: \n').lower() == 'E'

    # Perform Rail Fence Cipher operation
    result1 = railfence_cipher_encrypt(text, key, encrypt)

    # Display the result
    print('Result:', result1)

if __name__ == "__main__":
    main()

def main():
    # User inputs
    print('==========================================================\n')
    print('                DECRYPT YOUR CIPHER_TEXT\n                \n')
    print('==========================================================\n')
    ext = input('Enter the cipher_text: \n')
    key = int(input('Enter the relavant key: \n'))
    decrypt = input('Press D to decrypt your cipher_text: \n').lower() == 'd'

    # Perform Rail Fence Cipher operation
    result2 = railfence_cipher_decrypt(ext, key, decrypt)

    # Display the result
    print('Result:', result2)

if __name__ == "__main__":
    main()



 

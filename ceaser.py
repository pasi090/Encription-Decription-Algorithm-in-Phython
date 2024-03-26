import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('===Enter your text which you want to Encrypt or Decrypt:___ ').lower())

what_to_do = input('Enter Encrypt to ENC, Decrypt to DEC, exit to EXIT the program:___').lower()

shift_number = int(input('Enter your shift number/Key from 1 to 25: \n'))

end_program = False

while not end_program:
    # search through the enter text
    if what_to_do == 'enc':
        for i in range(len(sentence)):
            # get the position of each character within the sentence
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        # convert the list back to a string
        print(''.join(map(str, sentence)))
        end_program = True
    elif what_to_do == 'dec':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
            # convert the list back to a string
        print(''.join(map(str, sentence)))
        end_program = True
    else:
        decide = input(
            'invalid entry, try again Y for YES, N for NO: \n').lower()
        if decide == 'y':
            sentence = list(input('Enter your text: \n').lower())
            what_to_do = input(
                'Enter encrypt to ENC, decrypt to DEC, exit to EXIT the program \n').lower()
            shift_number = int(input('Enter your shift number from 1 to 25: \n'))
        else: 
            end_program = True
from morse import morse_code, morse_code_reverse

is_on = True

print("Welcome to Morse Code Converter!")
while is_on:
    type = input("Choose Morse Code 'encoding' or 'decoding': ").lower()
    if type == 'encoding' or type == 'encode':
        encode_str = input("Please enter your sentence(alphabet and number only).\n").upper()
        return_list = []
        flag = True
        for s in encode_str:
            if s != ' ':
                try:
                    return_list.append(morse_code[s])
                except KeyError:
                    print("The sentence you entered contains characters that are not alphabets or numbers.")
                    flag = False
                    break
            else:
                continue
        if flag:
            print(' '.join(return_list))

    elif type == 'decoding' or type == 'decode':
        code_list = input("Please enter your Morse code.\n").split(' ')
        return_list = []
        flag = True
        for code in code_list:
            try:
                return_list.append(morse_code_reverse[code])
            except KeyError:
                print("The code you enter contains wrong code.")
                flag = False
                break
        if flag:
            print(''.join(return_list))

    else:
        print("Wrong input. Please type again.")

    is_continue = input("Try again? (y/n): ")
    print()
    if is_continue != 'y':
        is_on = False

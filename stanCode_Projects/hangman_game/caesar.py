"""
File: caesar.py
Name: Cage
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:
    Use the secret number the access the new alphabet first, which can be applied to any secret numbers.
    Input the password, case-insensitive.
    To decode the ciphers, use for loop and find function to search the correspondent alphabet.
    n == -1 means the input units are not alphabets, such as space or !, so no need to transform them.
    """

    secret = int(input('Secret number: '))
    # obtain the new alphabet
    new_alphabet = ''
    for i in range(0, secret):
        new_alphabet += ALPHABET[26 - secret + i]
    for i in range(0, 26 - secret):
        new_alphabet += ALPHABET[i]
    # input the password
    password = input("What's the ciphered string? ")
    password = password.upper()
    # decode the ciphers
    ans = ''
    for i in range(len(password)):
        n = new_alphabet.find(password[i])
        if n == -1:
            ans += password[i]
        else:
            ans += ALPHABET[n]

    print('The deciphered string is: ' + str(ans))


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

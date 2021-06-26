"""
File: Substitution_Cipher_ext.py
Name: Cage
-----------------------------
This program use the concept of substitution cipher.
I use the secret code to form a set of alphabet sequence.
For example, if my SECRET is 'HELLO WORLD'.
The new set of sequence will be 'HELOWRDABCFGHIJKMNPQSTUVWXYZ', deleting the space and repetitive letters.
Therefore, if someone send me the message: 'USOPOTR'
And I type the correct secret code, for example: 'TSLA TO THE MOON'
I can decrypt the message as 'UBEREAT', so the sender must be hungry.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SECRET = 'TSLA TO THE MOON!'


def main():
    """
    TODO:
    First, the secret code is transformed to an upper case, no space, no punctuations,
    and no repetitive-letters sequence so that the secret code can be any sentence, phrase, or words.
    Therefore, a transform function is made to deal with the text.
    Then, my_enigma() will encrypt the message sent.
    If the secret code is correct, I can successfully decrypt the message.
    """
    # encrypt
    secret = transform(SECRET)
    message = input("Send Your Message: ").upper()
    encrypted_message = my_enigma(message, secret)
    print('The encrypted message received: ', encrypted_message)

    # decrypt
    secret_code = input('Secret Code: ')
    decrypted_message = my_decrypt(encrypted_message, secret_code)
    if decrypted_message == message:
        print('The message you decrypted is: ', decrypted_message)
    else:
        print('Your Code is Wrong')


def my_decrypt(encrypted_message, secret_code):
    """
    :param encrypted_message: str, the encrypted message from the my_enigma function.
    :param secret_code: str, the code necessary to break the message.
    :return: str, the decrypted message, same as original sent message.
    """
    find_sequence = ""
    find_sequence += transform(secret_code)
    for i in range(len(ALPHABET)):
        if ALPHABET[i] not in find_sequence:
            find_sequence += ALPHABET[i]
    deciphered = ""
    for i in range(len(encrypted_message)):
        n = find_sequence.find(encrypted_message[i])
        deciphered += ALPHABET[n]
    return deciphered


def my_enigma(message, secret):
    """
    :param message: str, the message sent.
    :param secret: str, the transformed code set at the beginning.
    :return:  str, the encrypted message.
    """
    new_alphabet = ''
    new_alphabet += secret
    for i in range(len(ALPHABET)):
        if ALPHABET[i] not in new_alphabet:
            new_alphabet += ALPHABET[i]
    password = ""
    for i in range(len(message)):
        n = ALPHABET.find(message[i])
        password += new_alphabet[n]
    return password


def transform(secret):
    """
    :param secret: str, the code needed to be transform
    :return: str, an upper-case sequence without space, punctuations, and repetitive letters.
    """
    result = ""
    # deal with case-insensitive
    secret = secret.upper()
    # delete space and punctuations
    for i in range(len(secret)):
        if secret[i].isalpha():
            result += secret[i]
        pass

    result1 = ""
    # delete repetitive letters
    for j in range(len(result)):
        n = result[0:j].find(result[j])
        if n == -1:
            result1 += result[j]
        pass
    return result1


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

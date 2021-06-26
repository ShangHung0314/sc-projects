"""
File: hangman.py
Name: Cage
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    I create a replace_dash function to replace the dash with the correct guessed number.
    The replace_dash function is built by a for loop, and I use [k:] to check if the input is in the answer.
    If the kth letter in the word is same with the input, replace the kth letter as the input.
    If not, save it as "_".
    """
    answer = random_word()
    dashed = ''
    dash = '_'
    n = 7
    for i in range(len(answer)):
        dashed += '_'
    print('The word looks like: ' + dashed)
    print('You have ' + str(n) + ' guesses left.')
    input_ch = input('Your guess: ')
    input_ch = input_ch.upper()

    while True:
        if input_ch.isdigit():
            print('Please type AN ALPHABET!')
            input_ch = input('Your guess: ')
            input_ch = input_ch.upper()
        elif len(input_ch) != 1:
            print('Please type ONLY ONE ALPHABET!')
            input_ch = input('Your guess: ')
            input_ch = input_ch.upper()
        # if guess wrong
        elif input_ch not in answer:
            print('There is no ' + input_ch + ' in the world')
            n -= 1
            # you thought you had the chance
            if n > 0:
                print('You have ' + str(n) + ' guesses left')
                input_ch = input('Your guess: ')
                input_ch = input_ch.upper()
            # but actually did not
            else:
                print('You are completely wrong :( ')
                print('The word was: ' + str(answer))
                break
        # if guess right
        else:
            print('You are correct!')
            for j in range(len(answer)):
                if input_ch == answer[j]:
                    dashed = replace_dash(dashed, dash, input_ch, answer)
            # vamos!
            if dash in dashed:
                print('The word looks like:' + dashed)
                input_ch = input('Your guess: ')
                input_ch = input_ch.upper()
            # finally!
            else:
                print('You win!')
                print('The word was: ' + dashed)
                break


def replace_dash(dashed, dash, input_ch, answer):
    """
    :param dashed: str, stored and used as the parameter each time in the loop.
    :param dash: str, "_"
    :param input_ch: str, the guessed number.
    :param answer: str, the answer generated randomly.
    :return: str, same length with the answer, the correct guess will be shown.
    """
    ans = ''
    for k in range(len(answer)):
        n = answer[k:].find(input_ch)
        if dashed[k] != dash:
            ans += dashed[k]
        elif dashed[k] == dash:
            if n == 0:
                ans += input_ch
            else:
                ans += dash
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

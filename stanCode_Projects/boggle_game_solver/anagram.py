"""
File: anagram.py
Name: Cage
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

dictionary = []  # list, store the dictionary
anagrams = []  # list, store the search results

possible = []  # list, store the words already searched, for pruning purpose
initial_index = []  # list, transform the dictionary into a list of first three letters of a word, for pruning purpose
initial_list = []  # list, all distinct first three letters in initial_index, for pruning purpose


def main():
    global possible, anagrams
    read_dictionary()
    initial_digit(dictionary)
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        search_word = str(input('Find anagrams for: ')).lower()
        start = time.time()
        if search_word == EXIT:
            break
        else:
            print('Searching...')
            ans = find_anagrams(search_word)
            print(len(ans), 'anagrams:', ans)
            end = time.time()
            print('Time: ', round(end - start, 2), 's')
            anagrams = []
            possible = []


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line.replace('\n', ''))


def find_anagrams(s):
    """
    :param s: str, the words to search
    :return: list, a list of anagrams found
    """
    search_list = []
    for ch in s:
        search_list.append(ch)
    anagrams_help(search_list, [], len(s))
    return anagrams


def anagrams_help(search_word, current_list, word_len):
    if len(current_list) == word_len and "".join(current_list) not in anagrams:
        word = "".join(current_list)
        if word in dictionary:
            anagrams.append(word)
            print('Found: ', word)
            print('Searching...')
    else:
        for ch in search_word:
            ## pruning ##
            # search sub_s
            # if a word is short, don't waste time search initials in the dict.
            if word_len > 6:
                if len(current_list) > 4:
                    if not has_prefix("".join(current_list)):
                        return
            # if a character repeat, do not search for it
            if "".join(current_list) in possible:
                return
            ## pruning ##

            # use pop(0) so that the character already chose won't be chose again
            ele = search_word.pop(0)

            # choose
            current_list.append(ele)

            # explore
            anagrams_help(search_word, current_list, word_len)
            possible.append("".join(current_list))

            # un-choose
            current_list.pop()

            search_word.append(ele)


def has_prefix(sub_s):
    """
    :param sub_s: str, the sub string that is currently searching
    :return: bool, whether the sub sting is in the dictionary
    TODO:
        Narrow the search range by searching through specific range in the dictionary.
        For example, if the input is contains, the program will search a range of words' first four letters with "cont".
        By testing different sets, search initial of four letters can result in the shortest time.
        The time searching for "contains" is now reduced to 7.2 seconds.
    """
    initial = sub_s[0:4]
    if initial not in initial_list:
        return False
    else:
        # get the next first three letters from initial list
        next_letter = initial_list[initial_list.index(initial) + 1]
    # If the input is contains, the search range in dictionary will be "cont" to"conu"
    # use initial_index to get the range of searching
    for i in range(initial_index.index(initial), initial_index.index(next_letter)):
        if str(dictionary[i]).startswith(str(sub_s)):
            return True


def initial_digit(d):
    """
    TODO:
        # to reduce the search range, transform the dictionary into a three letters index
        # ['a','aa','aah','aal','aar'...]
        # use set() function to remain the distinct item.
    """
    global initial_list, initial_index
    for i in range(len(d)):
        if len(d[i]) == 1:
            initial_index += d[i][0]
        elif len(d[i]) == 2:
            initial_index.append(d[i][0] + d[i][1])
        elif len(d[i]) == 3:
            initial_index.append(d[i][0] + d[i][1]+d[i][2])
        else:
            initial_index.append(d[i][0] + d[i][1] + d[i][2]+d[i][3])
    initial_list = sorted(list(set(initial_index)))


if __name__ == '__main__':
    main()

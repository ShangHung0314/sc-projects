"""
File: boggle.py
Name: Cage
----------------------------------------
TODO:
"""
import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

dictionary = []  # list, store the dictionary
ans = []  # list, store the answer
letter_list = []  # list, store the input letter
initial_list = []  # list, all distinct first three letters in initial_index, for pruning purpose
initial_index = []  # list, transform the dictionary into a list of first three letters of a word, for pruning purpose


def main():
    """
    TODO:
        [0 , 1, 2,  3
         4 , 5, 6,  7
         8 , 9, 10, 11
         12, 13 14, 15]
         [f, y, c, l
          i, o, m, g
          o, r, i, l
          h, j, h, u]
        I use a get_search_list function to get the list of the letter to search, given the already chose letter.
        Instead of storing string of letter in the current list, I store the index of letter into the list.
        For example, index 5 and 8 are both letter 'o', storing index will be easier to process.
        The shortest run time I test is 12.5 s.
    """
    read_dictionary()
    initial_digit(dictionary)
    for i in range(1, 5):
        ch = input(f'{i} row of letters: ').lower()
        if len(ch) != 7:
            print('Illegal input')
            break
        else:
            if not ch[0].isalpha() or not ch[2].isalpha() or not ch[4].isalpha() or not ch[6].isalpha():
                print('Illegal input')
                break
            elif not ch[1] == " " or not ch[3] == " " or not ch[5] == " ":
                print('Illegal input')
                break
            else:
                # for loop will be slow
                letter_list.append(ch[0])
                letter_list.append(ch[2])
                letter_list.append(ch[4])
                letter_list.append(ch[6])
    start = time.time()
    for i in range(len(letter_list)):
        boggle_helper(letter_list, [], i)
    end = time.time()
    print(f'There are {len(ans)} words in total.')
    print('Time: ', round(end - start, 2), 's')


def boggle_helper(letter_list, current_list, search_index):
    word = ""
    if len(current_list) >= 4:
        # transform indexes into letters
        for num in current_list:
            ch = letter_list[num]
            word += ch
        # pruning, I find put the function here resulting in the shortest run time
        short_dict_list = has_prefix(word)
        # if there is no initial in the dict: return; if has, return a shorten dict for search to reduce time.
        if short_dict_list is False:
            return
        else:
            if word in short_dict_list:
                if word not in ans:
                    ans.append(word)
                    print('Found ', word)
                    boggle_helper(letter_list, current_list, search_index)
                # find words longer than 4 characters -> if in ans, go through search_list and check
                else:
                    search_list = get_search_list(search_index, current_list)
                    for i in search_list:
                        word += letter_list[i]
                        if word in short_dict_list:
                            if word not in ans:
                                ans.append(word)
                                print('Found ', word)
                                search_index = i
                                current_list.append(i)
                                # keep finding words
                                boggle_helper(letter_list, current_list, search_index)
    else:
        search_list = get_search_list(search_index, current_list)
        for index in range(len(search_list)):
            if letter_list[index] not in current_list:
                # choose
                current_list.append(search_list[index])

                # explore
                search_index = search_list[index]
                boggle_helper(letter_list, current_list, search_index)

                # un-choose
                current_list.pop()


def get_search_list(index, current_list):
    """
    :param index: int, the index of currently chose letter
    :param current_list: list, current stored index, used to avoid choosing repeated letter
    :return:list, a list of letter should search next
    TODO:
        given the index, then return a list of index that the program should search
    """
    search_list = []
    for y in range(-1, 2, 1):
        for x in range(-1, 2, 1):
            s = index + x + 4 * y
            if 15 >= s >= 0:
                # the already chose letter won't be chose
                if s not in current_list:
                    # for column 2 & 3
                    if index % 4 == 1 or index % 4 == 2:
                        search_list.append(s)
                    # for column 1
                    elif index % 4 == 0:
                        if s % 4 == 0 or s % 4 == 1:
                            search_list.append(s)
                    # for column 4
                    elif index % 4 == 3:
                        if s % 4 == 2 or s % 4 == 3:
                            search_list.append(s)
    return search_list


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line.replace('\n', ''))


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    TODO:
        It's an improved version.
        Instead of return True, the function returns a shortened dict to search to reduce search time.
    """
    shorten = []
    initial = sub_s[0:3]
    if initial not in initial_list:
        return False
    else:
        next_letter = initial_list[initial_list.index(initial) + 1]
    for i in range(initial_index.index(initial), initial_index.index(next_letter)):
        # if str(dictionary[i]).startswith(str(sub_s)):
        #     return True
        shorten.append(dictionary[i])
    return shorten


def initial_digit(d):
    global initial_index, initial_list
    for i in range(len(d)):
        if len(d[i]) == 1:
            initial_index += d[i][0]
        elif len(d[i]) == 2:
            initial_index.append(d[i][0] + d[i][1])
        else:
            initial_index.append(d[i][0] + d[i][1] + d[i][2])
    initial_list = sorted(list(set(initial_index)))


if __name__ == '__main__':
    main()

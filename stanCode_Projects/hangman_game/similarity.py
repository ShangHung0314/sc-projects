"""
File: similarity.py
Name: Cage
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    If s2 is within s1, return it directly.
    If not, use (len(s1) - len(s2) + 1) to obtain how many sets of sequence to compare.
    Then, use if statement of s1[i+j] == s2[j] to check how many match in each set.
    Last, calculate which set has the highest correct ratio and indicate it in the variable match_set.
    """
    s1 = input("Please give me a DNA sequence to search: ")
    s1 = s1.upper()
    s2 = input("What DNA sequence would you like to match? ")
    s2 = s2.upper()
    ans = ''
    if s1.find(s2) != -1:
        ans += s2
        print('The best match is ' + str(ans))
    else:
        ratio = 0
        match_set = 0
        # (len(s1) - len(s2) + 1) sets to compare
        for i in range(len(s1) - len(s2) + 1):
            count = 0
            correct = 0
            for j in range(len(s2)):
                count += 1
                # s1[i + j] would allow us to move to next sets in s1 each round
                if s1[i + j] == s2[j]:
                    correct += 1
            # obtain the match set
            if correct / count > ratio:
                ratio = correct / count
                match_set = i
            # if no match at all, use match_set = -1 to separate it.
            else:
                match_set = -1
        if match_set != -1:
            ans += s1[match_set:(match_set + len(s2))]
            print('The best match is ' + str(ans))
        else:
            print('There is no match in the sequence')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()

"""
File: complement.py
Name: Cage
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    Transform the input DNA to uppercase first,
    then use the build_complement function to find the DNA's complement.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()
    complement = build_complement(dna)
    print('The complement of ' + str(dna) + ' is ' + str(complement))


def build_complement(dna):
    """
    :param dna: str, assume the input is the combination of A, T ,C ,or G.
    :return: The complement of the input DNA
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()

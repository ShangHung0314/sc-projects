"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
    :param n: int, a number to search for the largest digit
    :return: int, the largest digit
    """
    if n < 0:
        n *= -1
    largest = helper(n, 0)
    return largest


def helper(num, largest):
    """
    :param num: int, a positive number to search for the largest digit
    :param largest: int, to store the largest digit
    :return: int, the largest digit
    TODO:
        Use num - num // 10 * 10 to find the number of each digit
        and use the largest variable to store it.
    """
    # base case
    if 10 > num >= largest:
        return num
    # base case
    elif num <= largest:
        return largest
    else:
        if num - num // 10 * 10 > largest:
            largest = num - num // 10 * 10
        num = num // 10
        return helper(num, largest)


if __name__ == '__main__':
    main()

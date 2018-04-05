"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""


def check_permutation(string1, string2):
    """
    Checks if two strings are each others permutation

    Parameters
    ----------
    string1 : str
        First input string
    string2 :
        Second input strings

    Returns
    -------
    is_permutation : bool
        True if one string is a permutation of the other, otherwise False
    """
    is_permutation = True
    char_counts_1 = [0 for i in range(128)]
    char_counts_2 = [0 for i in range(128)]

    for c in string1:
        index = ord(c)
        char_counts_1[index] += 1

    for c in string2:
        index = ord(c)
        char_counts_2[index] += 1

    for i in range(len(char_counts_1)):
        total_count = char_counts_1[i] + char_counts_2[i]
        if total_count % 2 == 1:
            is_permutation = False

    return is_permutation


if __name__ == "__main__":
    print(check_permutation("abcd", "dbca"))
    print(check_permutation("abcda", "dbca"))

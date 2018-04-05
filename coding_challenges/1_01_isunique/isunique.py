"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


def is_unique(input_string):
    """
    Checks if a string all all unique characters, assuming the string contains ASCII characters.

    Parameters
    ----------
    input_string : str
        Input string consisting of English alphabets.

    Returns
    -------
    isunique : bool
        True if string contains unique characters, otherwise False
    """
    isunique = True

    char_counts = [0 for i in range(128)]
    for c in input_string:
        index = ord(c)
        if char_counts[index] == 0:
            char_counts[index] += 1
        else:
            isunique = False
            break

    return isunique


if __name__ == "__main__":
    print(is_unique("abcd"))
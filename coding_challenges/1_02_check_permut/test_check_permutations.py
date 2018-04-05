"""
Tests for check_permutations.py
"""
from check_permutations import check_permutation


def test_permutation_strings():
    assert check_permutation("abcd", "dbca")


def test_non_permutation_strings():
    assert not check_permutation("abcda", "dbca")
    
"""
Test script for isunique.py
"""

from isunique import is_unique

def test_nonunique_string():
    assert not is_unique("kamran")

def test_unique_string():
    assert is_unique("pytorch")

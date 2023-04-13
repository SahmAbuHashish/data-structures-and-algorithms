import pytest
from array_binary_search import BinarySearch

def test_BinarySearch_1():

    actual = BinarySearch([4, 8, 15, 16, 23, 42], 15)
    expected = 2
    assert actual == expected
#------------------------------------------
def test_BinarySearch_2():

    actual = BinarySearch([-131, -82, 0, 27, 42, 68, 179], 42)
    expected = 4
    assert actual == expected
#------------------------------------------
def test_BinarySearch_3():

    actual = BinarySearch([11, 22, 33, 44, 55, 66, 77], 90)
    expected = -1
    assert actual == expected
#------------------------------------------
def test_BinarySearch_4():

    actual = BinarySearch([1, 2, 3, 5, 6, 7], 4)
    expected = -1
    assert actual == expected


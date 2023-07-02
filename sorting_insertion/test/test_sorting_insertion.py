import pytest
from sorting_insertion.sorting_insertion import sorting_insertion


def test_sorting_insertion():
   # Sample arrays
    input1 = [8, 4, 23, 42, 16, 15]
    input2 = [20, 18, 12, 8, 5, -2]
    input3 = [5, 12, 7, 5, 5, 7]
    input4 = [2, 3, 5, 7, 13, 11]

    # Test case 1: Sample array [8, 4, 23, 42, 16, 15]
    assert sorting_insertion(input1) == [4, 8, 15, 16, 23, 42]

    # Test case 2: Reverse-sorted array [20, 18, 12, 8, 5, -2]
    assert sorting_insertion(input2) == [-2, 5, 8, 12, 18, 20]

    # Test case 3: Few uniques array [5, 12, 7, 5, 5, 7]
    assert sorting_insertion(input3) == [5, 5, 5, 7, 7, 12]

    # Test case 4: Nearly-sorted array [2, 3, 5, 7, 13, 11]
    assert sorting_insertion(input4) == [2, 3, 5, 7, 11, 13]
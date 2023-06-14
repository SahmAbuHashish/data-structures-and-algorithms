import pytest
from sorting_merge.sorting_merge import merge_sort

# Test Cases
def test_empty_array():
    arr = []
    merge_sort(arr)
    assert arr == []

def test_single_element():
    arr = [8]
    merge_sort(arr)
    assert arr == [8]

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_duplicate_elements():
    arr = [3, 2, 1, 2, 3]
    merge_sort(arr)
    assert arr == [1, 2, 2, 3, 3]

def test_large_array():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_mixed_positive_negative():
    arr = [4, -3, 2, -1, 0, -2]
    merge_sort(arr)
    assert arr == [-3, -2, -1, 0, 2, 4]
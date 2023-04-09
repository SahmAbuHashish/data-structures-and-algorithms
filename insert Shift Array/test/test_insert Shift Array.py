import pytest

from insert_Shift_Array import insertShiftArray

def test_insert_Shift_Array():
    actual = insertShiftArray([2,4,6,-8], 5)
    expected = [2,4,5,6,-8]
    assert actual == expected
    
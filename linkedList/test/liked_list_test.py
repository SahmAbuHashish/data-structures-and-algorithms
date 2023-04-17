import pytest
from linkedList.linked_list import Linked_list

def test_empty_liked_list():
    likedList = Linked_list()
    excepted = "Empty LinkedList"
    actual = str(likedList) 
    assert excepted == actual

# def test_append_node(likedList):
#     excepted = "5 --> sahm --> 2.5 --> None" 
#     actual = str(likedList)
#     assert excepted == actual

def test_linked_list_insert():
    likedList = Linked_list()
    likedList.insert("a")
    actual = likedList.head.value
    expected = "a"
    assert actual == expected

def test_linked_list_includes(likedList):
    actual = likedList.includes("a")
    expected = True
    assert actual == expected

    actual = likedList.includes("c")
    expected = False
    assert actual == expected    

def test_linked_list_to_string(likedList):
    assert likedList.to_string() == "{ a } -> { b } -> { c } -> NULL"    

@pytest.fixture
def likedList():
    likedList = Linked_list()
    likedList.insert('a')
    likedList.insert('b')
    likedList.insert('c')
    return likedList

import pytest
from linked_list_insertions import LinkedList

def test_empty_liked_list():
    likedList = LinkedList()
    excepted = "Empty LinkedList"
    actual = str(likedList) 
    assert excepted == actual

def test_append_node(likedList):
    excepted = "a --> b --> c --> None" 
    actual = str(likedList)
    assert excepted == actual

def test_linked_list_insert():
    likedList = LinkedList()
    likedList.insert("a")
    actual = likedList.head.value
    expected = "a"
    assert actual == expected

def test_linked_list_includes(likedList):
    likedList = LinkedList()
    actual = likedList.includes("a")
    expected = True
    assert actual == expected

    actual = likedList.includes("c")
    expected = False
    assert actual == expected    

   

@pytest.fixture
def likedList():
    likedList = LinkedList()
    likedList.insert('a')
    likedList.insert('b')
    likedList.insert('c')
    return likedList
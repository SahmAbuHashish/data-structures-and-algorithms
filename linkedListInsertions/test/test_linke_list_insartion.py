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

def test_linked_zip_list():
    linked_list1 = LinkedList()
    linked_list1.append("a")
    linked_list1.append("b")
    linked_list1.append("c")
    linked_list2 = LinkedList()
    linked_list2.append("a")
    linked_list2.append("b")
    linked_list2.append("c")
    linked_list3 = zip_lists(linked_list1,linked_list2)
    actual = linked_list3.__str__()
    expected = "{ a } -> { a } -> { b } -> { b } -> { c } -> { c } -> Null"
    assert actual == expected   

@pytest.fixture
def likedList():
    likedList = LinkedList()
    likedList.insert('a')
    likedList.insert('b')
    likedList.insert('c')
    return likedList
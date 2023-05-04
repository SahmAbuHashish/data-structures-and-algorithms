import pytest
from  stack_and_queue import Queue,Stack

def test_enqueue_single_value():
    q = Queue()
    q.enqueue(1)
    assert str(q) == "1 --> None"

def test_enqueue_multiple_values():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert str(q) == "1 --> 2 --> 3 --> None"

def test_dequeue_single_value():
    q = Queue()
    q.enqueue(1)
    assert q.dequeue() == 1

def test_peek():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1

def test_empty_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.dequeue()
    assert q.is_empty() == True

def test_instantiate_empty_queue():
    q = Queue()
    assert q.is_empty() == True

def test_dequeue_empty_queue():
    q = Queue()
    with pytest.raises(Exception):
        q.dequeue()

def test_peek_empty_queue():
    q = Queue()
    with pytest.raises(Exception):
        q.peek()
#------------------------------------------
def test_push_one():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.peek() == 1

def test_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False
    stack.pop()
    assert stack.is_empty() == True

def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()

def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()        
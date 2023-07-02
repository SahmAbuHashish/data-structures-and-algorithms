import pytest
from  stack_and_queue import PseudoQueue

def test_pseudo_queue_enqueue_1():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue('a')
    pseudo_queue.enqueue('b')
    pseudo_queue.enqueue('c')

    expected = "{ c } -> { b } -> { a } -> Null"
    actual = str(pseudo_queue.stack1)
    assert actual == expected

def test_pseudo_queue_dequeue_1():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue('a')
    pseudo_queue.enqueue('b')
    pseudo_queue.enqueue('c')
    pseudo_queue.enqueue()

    expected = "{ b } -> { c } -> Null"
    actual = str(pseudo_queue.stack2)
    assert actual == expected


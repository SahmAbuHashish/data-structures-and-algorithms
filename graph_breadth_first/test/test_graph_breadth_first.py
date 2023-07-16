import pytest
from graph.graph import Graph
from graph_breadth_first.graph_breadth_first import breadth_first

def test_bfs_simple_connected_graph():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    bfs_order = breadth_first(graph, 1)
    assert bfs_order == [1, 2, 3, 4]

    bfs_order = breadth_first(graph, 3)
    assert bfs_order == [3, 1, 2, 4]


def test_bfs_disconnected_graph():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)

    bfs_order = breadth_first(graph, 1)
    assert bfs_order == [1, 2]

    bfs_order = breadth_first(graph, 3)
    assert bfs_order == [3, 4]


def test_bfs_graph_with_loops():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(1, 1)  
    graph.add_edge(2, 2)  
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    bfs_order = breadth_first(graph, 1)
    assert bfs_order == [1, 2, 3]

    bfs_order = breadth_first(graph, 2)
    assert bfs_order == [2, 1, 3]


def test_bfs_large_graph():
    graph = Graph()
    for i in range(1, 1001):
        graph.add_vertex(i)
        if i > 1:
            graph.add_edge(i, i-1)


    bfs_order = breadth_first(graph, 1)
    assert bfs_order == list(range(1, 1001))
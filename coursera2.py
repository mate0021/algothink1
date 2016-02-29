"""
Script containing Homework2
"""

from collections import deque
# from test_graphs import *

TEST_GRAPH1 = {
    1: {4},
    2: {4},
    3: {4},
    4: {1, 2, 3, 6},
    5: {7},
    6: {4},
    7: {5, 8},
    8: {7},
    9: set([])
}

TEST_GRAPH_SINGLES = {
    1: set([]),
    2: set([]),
    3: set([]),
    4: set([])
}

def bfs_visited(ugraph, start_node):
    """
    Visits every possible node starting from start_node
    :param ugraph:
    :param start_node:
    :return: Set of nodes that were visited
    """
    result = set()
    queue = deque()
    queue.append(start_node)
    result.add(start_node)

    while len(queue) > 0:
        node = queue.pop()
        for neighbour in ugraph[node]:
            if neighbour not in result:
                result.add(neighbour)
                queue.append(neighbour)

    return result

from2 = bfs_visited(TEST_GRAPH1, 2)
from4 = bfs_visited(TEST_GRAPH1, 4)
from7 = bfs_visited(TEST_GRAPH1, 7)
from9 = bfs_visited(TEST_GRAPH1, 9)

# print(str(from2 == {1, 2, 3, 4, 6}) + " " + str(from2))
# print(str(from4 == {1, 2, 3, 4, 6}) + " " + str(from4))
# print(str(from7 == {5, 7, 8}) + " " + str(from7))
# print(str(from9 == {9}) + " " + str(from9))

def cc_visited(ugraph):
    """
    Takes a graph and returns a list of connected components.
    :param ugraph:
    :return: a list of sets
    """
    result = []
    nodes = ugraph.keys()

    for node in nodes:
        ccs = bfs_visited(ugraph, node)
        if ccs not in result:
            result.append(ccs)
        nodes = set(nodes) - ccs

    return result

cc1 = cc_visited(TEST_GRAPH1)
# print(str(cc1 == [{1, 2, 3, 4, 6}, {5, 7, 8}, {9}]) + " " + str(cc1))

# def func(a_list):
#     return sum(a_list)

def largest_cc_size(ugraph):
    """
    Gets size of the largest of connected components.
    :param ugraph:
    :return:
    """
    max_size = 0
    for sub in cc_visited(ugraph):
        if max_size < len(sub):
            max_size = len(sub)

    return max_size

TEST_GRAPH2 = {
    1: {2},
    2: {1},
    3: {4},
    4: {5},
    5: {4}
}

# print(str(largest_cc_size(TEST_GRAPH2) == 3))



def compute_resilience(ugraph, attack_order):
    """
    Remove nodes one by one from the graph.
    :param ugraph:
    :param attack_order:
    :return:
    """
    result = [largest_cc_size(ugraph)]
    for node in attack_order:
        removed = __remove_node(ugraph, node)
        result.append(largest_cc_size(removed))

    return result

def __remove_node(ugraph, node_to_delete):
    """
    From a graph, remove the node and all edges connected to it.
    :param ugraph:
    :param node_to_delete:
    :return:
    """
    del ugraph[node_to_delete]
    for node in ugraph.keys():
        ugraph[node] -= {node_to_delete}

    return ugraph

# 1---2
# | \
# 3---4
TEST_REMOVE_GRAPH = {
    1: {2, 3, 4},
    2: {1},
    3: {1, 4},
    4: {1, 3}
}

# 1---2
#   \
#     4
EXPECTED = {
    1: set([2, 4]),
    2: set([1]),
    4: set([1])
}
removed3 = __remove_node(TEST_REMOVE_GRAPH, 3)
# print(removed3 == EXPECTED, str(removed3))

# print(compute_resilience(TEST_GRAPH1, [4]))
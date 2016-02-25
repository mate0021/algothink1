"""
Script containing Homework2
"""
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
from collections import deque

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
    return max(cc_visited(ugraph))

# print(str(largest_cc_size(TEST_GRAPH1) == {1, 2, 3, 4, 6}))

def compute_resilience(ugraph, attack_order):
    for node in attack_order:
        pass

def __remove_node(ugraph, node_to_delete):
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


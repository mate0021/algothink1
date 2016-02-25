"""
Script containing sample for 1st homework
"""
EX_GRAPH0 = {0: {1, 2}, 1: set([]), 2: set([])}
EX_GRAPH1 = {
    0: {1, 4, 5},
    1: {2, 6},
    2: {3},
    3: {0},
    4: {1},
    5: {2},
    6: set([])
}
EX_GRAPH2 = {
    0: {1, 4, 5},
    1: {2, 6},
    2: {3, 7},
    3: {7},
    4: {1},
    5: {2},
    6: set([]),
    7: {3},
    8: {1, 2},
    9: {0, 3, 4, 5, 6, 7}
}

def make_complete_graph(num_nodes):
    """
    :param num_nodes: Number of nodes for the graph
    :return:
    """
    if num_nodes <= 1:
        return set([])
    result = {}
    for key in range(0, num_nodes):
        result[key] = [value for value in range(0, num_nodes) if key != value]

    return result

def compute_in_degrees(graph):
    """
    Compute for each node what is the in degree
    :param graph:
    :return:
    """
    result = {}
    for key in graph.keys():
        result[key] = 0
    for key in graph.keys():
        for value in graph[key]:
            result[value] = result.get(value, 0) + 1

    return result

def in_degree_distribution(graph):
    """
    :param graph:
    :return:
    """
    result = {}
    degrees = sorted(compute_in_degrees(graph).values())
    for degree in degrees:
        result[degree] = result.get(degree, 0) + 1

    return result

# print EX_GRAPH2
# print compute_in_degrees(EX_GRAPH2)
# print in_degree_distribution(EX_GRAPH2)
print make_complete_graph(4)
import sys
sys.path.append('../graph')

''' Find the earliest ancestor of a node '''


def earliest_ancestor(ancestors, starting_node):
    # Create graph
    graph = Graph()

    # Add vertices
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
    # Add edges, direction child > parent
    for parent, child in ancestors:
        graph.add_edge(child, parent)

    # if vert has no parent (eg, not empty set)
    # return -1

if not graph.get_neighbors(starting_node):
    return -1
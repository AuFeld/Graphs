# Understood

# Plan
## Graphs Problem Solving
### Translate the problem
#### Nodes = people
#### Edges = when child has a parent

### build our graph, or define our get_neighbors

### choose algo
#### either BFS or DFS

''' BFS ''' 

import sys
sys.path.append('../graph')

from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    # Lets create our dictionary to store parents for each child
    parents = {}
    # Now we're creating our empty queue and enqueue
    # A path to our starting node
    q = Queue()
    q.enqueue([starting_node])

    for a in ancestors:
        # key
        k = a[1]
        # value
        v = a[0]
        if k not in parents:
            parents[k] = []
        parents[k].append(v)

    # Second, will list to keep track of len from our longest path and node at that length
    longest = [0, 0]
    # While our queue is not empty:
    while q.size() > 0:
        # Dequeue our first path
        path = q.dequeue()
        # will now grab our last node from the path
        node = path[-1]
        # lets check if node has parents within our dictionary:
        if node not in parents:
          # if our, will now compare length of our current path to store longest.
            # in addition, node at the distance
            if len(path) > longest[0]:
                longest = (len(path), node)
            elif len(path) == longest and longest[1] > node:
                longest = (len(path), node)

        else:
            # if we have parents in the dict, will add a new path for each
            # parent of our last_vertex:brea
            for parent in parents[node]:
                q.enqueue(path + [parent])
    # if our starting node does not  have any parents, will return -1:
    if longest[1] == starting_node:
        return -1
    else:
        # if not, our earliest ancestor  will be should stored in longest
        return longest[1]

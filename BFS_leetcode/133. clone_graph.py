"""
- 1. use a hashmap to store the reference of the copy of all the nodes that have already been visited and copied.
     The [key] for the hash map would be the node of the original graph and corresponding. [value] would be the corresponding
     cloned node of the cloned graph. 
     The [visited] is used to prevent cycles and get the cloned copy of a node 

- 2. Add the first node to the queue. Clone the first node and add it to [visited] hashmap
- 3. Do the BFS traversal:
    - pop a node from the front of the queue
    - visit all the neighbors of this node
    - if any of the neighbors was already visited then it must be present in the [visited] dictionary
      get the clone of this neighbor from visited in that case
    - otherwise, create a clone and store in the visited
    - add the clones of the neighbors to the corresponding list of the clone node 
"""


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


from collections import deque


class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        # dictionary to save the visited node and it's respective clone as key
        # and value respectively. This helps to avoid cycles
        visited = {}

        # put the first node in the queue
        queue = deque([node])
        # clone the node and put it in the visited dictionary
        visited[node] = Node(node.val, [])

        # BFS
        while queue:
            # pop a node say 'n' from the front of the queue
            n = queue.popleft()
            # iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node 'n'
                visited[n].neighbors.append(visited[neighbor])
        # return the clone of the node from visited
        return visited[node]
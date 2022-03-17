"""
if a node is not already visited, try bfs from this node, add the count of connected components by 1
"""
import collections


def countComponents(n, edges):
    graph = collections.defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def bfs(node, seen):
        queue = collections.deque([node])
        while queue:
            for neighbor in graph[node]:
                if neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

    count = 0
    seen = set()
    for node in range(n):
        if node not in seen:
            seen.add(node)
            bfs(node, seen)
            count += 1
    return count

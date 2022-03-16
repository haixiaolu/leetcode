import collections


def ValidTree(n, edges):
    if len(edges) != n - 1:
        return False

    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    parent = {0: -1}
    queue = collections.deque([0])

    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if neighbor == parent[node]:
                continue
            if neighbor in parent:
                return False
            parent[neighbor] = node
            queue.append(neighbor)
    return len(parent) == n

"""
DFS
使用深度优先遍历， 统计可以到达的节点个数，并利用集合visited标记当前节点是否访问过，以防止重复访问
- 先找第0个房间的第一个钥匙
- 进入那个房间， 在找它的第一个钥匙
- 重复以往， 知道没钥匙了， 那么退回刚刚的房间
- 找刚刚房间的第二把钥匙
- 重复以往
"""
import collections


def canVisitedAllRooms(rooms):
    def dfs(x):
        visited.add(x)
        nonlocal num
        num += 1
        for key in rooms[x]:
            if key not in visited:
                dfs(key)

    n = len(rooms)
    num = 0
    visited = set()
    dfs(0)
    return num == n


## Time: O(n + m)

# BFS
def canVisitedAllRooms(rooms):
    n = len(rooms)
    num = 0
    visited = set()
    queue = collections.deque([0])
    while queue:
        x = queue.popleft()
        num += 1
        for key in rooms[x]:
            if key not in visited:
                visited.add(key)
                queue.append(key)
    return num == n

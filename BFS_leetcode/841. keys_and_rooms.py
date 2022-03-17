"""
- 首先找到0号房间， 把所有0号房间的钥匙都开一遍
- 进入刚刚开过的房间， 再把所有房间里的钥匙再开一遍
- 重复以往， 层层递进， 直到找不到符合要求的节点
"""


def canVisitedAllRooms(rooms):
    visited = {0}
    queue = [0]

    while queue:
        room_index = queue.pop()
        for key in rooms[room_index]:
            if key not in visited:
                visited.add(key)
                queue.insert(0, key)
    return len(visited) == len(rooms)
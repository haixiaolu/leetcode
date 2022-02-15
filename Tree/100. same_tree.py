"""
- if both of the tree is empty, same
- if one of the tree is empty, not same
- if both are not empty
    -- first to check if the root is same
        -- if not same, not a same tree
        -- if same, then check the left and right child
- recursively
"""
import collections


def isSameTree(p, q):
    # DFS
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# BFS
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    queue1 = collections.deque([p])
    queue2 = collections.deque([q])

    while queue1 and queue2:
        node1 = queue1.popleft()
        node2 = queue2.popleft()
        if node1.val != node2.val:
            return False
        left1, right1 = node1.left, node1.right
        left2, right2 = node2.left, node2.right
        if (not left1) ^ (not left2):
            return False
        if (not right1) ^ (not right2):
            return False
        if left1:
            queue1.append(left1)
        if right1:
            queue1.append(right1)
        if left2:
            queue2.append(left2)
        if right2:
            queue2.append(right2)
    return not queue1 and not queue2

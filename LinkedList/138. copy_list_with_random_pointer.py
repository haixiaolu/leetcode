# two passes with hashmap
class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None: None}

        # first pass, colone the node
        cur = head
        while cur:
            # create copy of node
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
from unittest.mock import NonCallableMagicMock


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy

        while pointer != None:
            node = pointer

            for i in range(k):
                if node:
                    node = node.next
            if not node:
                break

            prev = None
            curr = pointer.next
            next = None
            for i in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            tail = pointer.next
            tail.next = curr
            pointer.next = prev
            pointer = tail

        return dummy.next

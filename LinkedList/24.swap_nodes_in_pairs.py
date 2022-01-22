class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        dummyHead = ListNode(-1)
        pre = dummyHead
        p = head

        while p and p.next:
            q = p.next

            pre.next = q
            p.next = q.next
            q.next = p

            pre = p
            p = p.next

        return dummyHead.next

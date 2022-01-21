class Solution:
    def removeElements(self, head, val):

        # iteration（迭代）
        # dummyHead = ListNode(0)
        # dummyHead.next = head
        # temp = dummyHead
        # while temp.next:
        #     if temp.next.val == val:
        #         temp.next = temp.next.next
        #     else:
        #         temp = temp.next
        # return dummyHead.next

        # recursion(递归)
        if head is None:
            return head

        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head

def partition(self, head, x):
    left, right = ListNode(), ListNode()
    ltail, rtail = left, right

    while head:
        if head.val < x:
            ltail.next = head
            ltail = head.next

        else:
            rtail.next = head
            rtail = head.next

        head = head.next

    # connect two list
    ltail.next = right.next
    right.next = None
    return left.next

def isPalindrome(self, head):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    left, right = head, prev
    while left:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

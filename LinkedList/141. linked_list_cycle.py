# two pointers, fast pointers move two step, slow move one step
# if they meet, cycle, otherwise no cycle


def hasCycle(head):
    if not head or not head.next:
        return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


# hashset
def hasCycle(self, head):

    hashset = set()

    while head:
        if head in hashset:
            return True
        hashset.add(head)
        head = head.next

    return False

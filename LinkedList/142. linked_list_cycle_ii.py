# hashset

# def detectCycle(self, head):

#     position = head
#     visited = set()

#     while position:
#         if position in visited:
#             return position
#         else:
#             visited.add(position)

#         position = position.next

#     return None

# two pointer


def detectCycle(self, head):

    if not head:
        return None

    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        # when two pointers meet
        if fast == slow:
            fast = head

            while fast != slow:
                fast = fast.next
                slow = slow.next

            return fast

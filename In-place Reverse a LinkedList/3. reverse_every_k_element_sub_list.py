# leetcode 25. Reverse Nodes in K Groups
"""
Given the head of a LinkedList and a number 'k', reverse every 'k' sized sub-list starting from the head.
If in the end, you are left with a sub-list with less than 'k' elements, reverse it too
"""
"""
Approach:
    - It is quite similar to Reverse a sub-list.
    - The only difference is that we have to reverse all the sub-lists. We can use the same approach,
      starting with the first-sub-list(i.e.,p = 1, q=k) and keep reversing all the sublists of size 'K'
"""


class Solution:
    def reverseKGroup(self, head, k):
        if k <= 1 or head is None:
            return head

        current = head
        previous = None
        while True:
            last_node_of_previous_part = previous
            # after reversing the LinkedList 'current' will become the last node of the sub-list
            last_node_of_sub_list = current
            next = None  # will be used to temporarity store the next node
            i = 0
            while current is not None and i < k:  # reverse 'k' nodes
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1
            # connect with the previous part
            if last_node_of_previous_part is not None:
                last_node_of_previous_part.next = previous
            else:
                head = previous

            # connect with the next part
            last_node_of_sub_list.next = current

            if current is None:
                break
            previous = last_node_of_sub_list
        return head
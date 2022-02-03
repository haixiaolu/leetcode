# leetcode 92. Reverse LinkedList II
"""
Given the head of a LinkedList and two pointers 'p' and 'q', reverse the LinkedList from position p to q 
"""
"""
Approach:
Use similar approach as in Reverse LinkedList 
    - skip the first p - 1 node, to reach the node at position p 
    - Remember the node at position p - 1 to be used later to connect with the reversed sub-list
    - Next, reverse the nodes from p to q using the same approach in Reverse LinkedList 
    - connect the p - 1 and q + 1 nodes to the reversed sub-list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, p: int, q: int) -> ListNode:
        if p == q:
            return head

        # after skipping 'p - 1' nodes, current will point to 'p'th node
        current, previous = head, None
        i = 0
        while current is not None and i < p - 1:
            previous = current
            current = current.next
            i += 1

        # We are interested in three parts of the LinkedList, the part before index 'p'
        # the part between 'p' and 'q', and the part after index 'q'
        last_node_of_first_part = previous
        # after reversing the LinkedList 'current' will become the last node of the sublist
        last_node_of_sub_list = current
        next = None  # will be used to temporarity store the next node

        i = 0
        # reverse nodes between p and q
        while current is not None and i < q - p + 1:
            next = current.next
            current.next = previous
            previous = current
            current = next

        # connect with the first part
        if last_node_of_first_part is not None:
            # previous is now the first node of the sub_list
            last_node_of_sub_list.next = previous
        # this means p == 1 (we are changing the first node(head) of the linkedlist)
        else:
            head = previous

        # connect with the last part
        last_node_of_sub_list.next = head
        return head

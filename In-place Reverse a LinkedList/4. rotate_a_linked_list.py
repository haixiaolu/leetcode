# leetcode 61. Rotate List
"""
Given the head of a Singly LinkedList and a number 'k', rotate the LinkedList to the right by 'k' notes
"""
"""
Approach:
 - Another way of defining the rotation is to take the sub-list of 'k' ending nodes of the Linkedlist and connect
   them to the beginning. Other than that we have to do three more things:
   - Connect the last node of the LinkedList to the head, because the list will have a different tail after the rotation
   - The new head of the LinkedList will be the node at the beginning of the sublist
   - The node right before the start of sub-list will be the new tail of the rotated LinkedList 
"""


def rotatedRight(head, k):
    if head is None or head.next is None or k <= 0:
        return head

    # find the length and the last node of the list
    last_node = head
    list_length = 1
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    last_node.next = (
        head  # connect the last node with the head to ake it a circular list
    )
    k %= list_length  # no need to do rotations more than the length of the list
    skip_length = list_length - k
    last_node_of_rotated_list = head
    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next

    # last_node_of_rotated_list.next is pointing to the sub-list of 'k' ending nodes
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None
    return head

# leetcode 206. Reverse a Linked List
"""
Given the head of Singly Linked List, reverse the LinkedList, Write a function to return the new head
of the reversed LinkedList 
"""
"""
Approach:
    1. Reverse one node at a time
    2. Start with a variable cur which will initially point to the head 
    3. Start with a variable prev which will point to the previous node, initially previous will point to null
    4. In a stepwise manner, reverse the cur node by pointing it to the previous before moving on to the next node
    5. update the previous to alway point to the previous node that we have processed
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    cur = head
    prev = None

    while cur is not None:
        next = cur.next  # temporarity store the next node
        cur.next = prev  # reverse the current node
        prev = cur  # before we move to the next node, point previous to cur
        cur = next  # move to the next node
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", result)


main()

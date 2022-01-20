# hashset
# def getIntersectionNode(self, headA, headB):
#     visited = set()
#     temp = headA
#     while temp:
#         visited.add(temp)
#         temp = temp.next

#     temp = headB
#     while temp:
#         if temp in visited:
#             return temp

#         temp = temp.next

#     return None

# two pointers
def getIntersectionNode(headA, headB):
    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


headA = [1, 2, 3, 4, 5]
headB = [7, 8, 9, 4, 10]

obj = getIntersectionNode(headA, headB)
print(obj)

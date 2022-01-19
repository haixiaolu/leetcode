# 设定一个哨兵节点， prehead
# 维护一个prev指针


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        # 维护一个prev指针
        prev = prehead

        # 直到l1或这l2指向null， 如果l1当前节点的值小于l2
        # 我们就把l1当前的节点接在prev节点的后面
        # 同时l1往后移一位， l2同样的操作
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        # 合并l1和l2后，最多只有一个还未被合并完，我们直接将链表
        # 末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2
        return prehead.next

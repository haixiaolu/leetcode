"""
Question: given the heads of two sorted linked list list1 and list2
          merge the two lists in a one sorted list. the list should be made by splicing together the nodes of the first two lists

          Return the head of the merged linked list

         Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
         Output: [1, 1, 2, 3, 4, 4]
"""

"""
Approach: 递归
 merge 操作：
          - list1[0] + merge[list1[1:], list2] list1[0] < list2[0]
          - list2[0] + merge[list1, list2[1:]] otherwise

          1. 如果l1或者l2一开始是空列表， 没有任何操作的需要合并， 返回空列表
          2. 我们判断l1和l2那一个链表的头节点的值更小， 然后递归的决定下一个添加到结果里的节点
          3. 如果两个链表右一个为空， 递归结束
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Time: O(n + m)
# Space: O(n + m), n和m分别为两个链表的长度。 递归调用mergeTwoLists函数时需要消耗栈空间，
#                   栈空间的大小取决于递归调用的深度。

"""
Method 2: 迭代

    - 首先， 我们设定一个哨兵节点 prehead， 这可以在最后让我们比较容易地返回合并后的链表。 
    - 我们维护一个prev指针， 我们需要做的事调整它的next指针， 然后， 我们重复以下过程， 知道l1或者l2指向了null：
        -- 如果l1当前节点的值小于等于l2， 我们就把l1当前的节点接在prev节点的后面同时将l1指针往后移一位。
        -- 否则， 我们对l2做同样的操作， 不管我们将那一个元素接在了后面， 我们都需要把prev向后移一位
    - 在循环终止时， l1和l2至多右一个是非空的，由于输入的两个链表都是有序的， 所以不管那个链表是非空的， 它包含的所有元素都比前面已经合并链表中的的所有元素都要大
      这意味着我们只需要简单地将非空链表接在合并链表的后面， 并返回合并链表即可
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后l1和l2最多只有一个还未被合并完， 我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next


# Time: O(n + m)
# Space: O(1)
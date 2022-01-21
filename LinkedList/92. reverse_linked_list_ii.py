# based on 206 reverse Linked List, reverse left and right parts, then connect them together
# we need to track one node before left and one node after right
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        # 穿针引线
        # def reverse_linked_list(head: ListNode):
        #     # 也可以递归反转一个链表
        #     prev = None
        #     cur = head
        #     while cur:
        #         next = cur.next
        #         cur.next = prev
        #         prev = cur
        #         cur = next

        # # 因为头节点有可能发生变化， 使用虚拟头节点可以避免复杂的分类讨论
        # dummy_node = ListNode(-1)
        # dummy_node.next = head
        # prev = dummy_node

        # # 第一步： 从虚拟头节点走left - 1步， 来到left节点的前一个节点
        # # 写在for循环里，语义清晰
        # for _ in range(left - 1):
        #     prev = prev.next

        # # 第二步：从prev再走right - left + 1步， 来到right节点
        # right_node = prev
        # for _ in range(right - left + 1):
        #     right_node = right_node.next

        # # 第三步： 切断出一个子链表
        # left_node = prev.next
        # curr = right_node.next

        # # 注意， 切断链接
        # prev.next = None
        # right_node.next = None

        # # 第四步
        # reverse_linked_list(left_node)

        # # 第五步
        # prev.next = right_node
        # left_node.next = curr
        # return dummy_node.next

        # 一次遍历
        dummy_node = ListNode(-1)
        dummy_node.next = head
        prev = dummy_node
        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next
        return dummy_node

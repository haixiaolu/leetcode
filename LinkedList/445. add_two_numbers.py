# use stack


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # 建立用于l1和l2个结点的值
        stack1 = []
        stack2 = []

        # 将l1入栈
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        ans = None
        carry = 0

        # 循环跌点直到栈为空或者进位为空
        while stack1 or stack2 or carry != 0:
            # 使用临时变量来记录出栈的值
            a = 0 if not stack1 else stack1.pop()
            b = 0 if not stack2 else stack2.pop()
            current = a + b + carry
            carry = current // 10
            current % 10

            # 头插法
            cur_node = ListNode(current)
            cur_node.next = ans
            ans = cur_node

        return ans

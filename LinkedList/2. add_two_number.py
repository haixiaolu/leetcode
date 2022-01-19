# 同时遍历两个链表， 逐位计算它们的和， 并于当前位置的进位值相加
# 需要保存进位， 需要保存结果
# 结束时：
# 两个链表只要有一个非空就需要往后进行
# 如果遍历结束， 进位不为0， 需要把进位项添加在链表的后面


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # 将当前节点初始化为返回链表的哑结点
        head = point = ListNode(0)
        carry = 0  # 进位初始化为0

        # 遍历两个链表
        while l1 or l2:
            new_point = ListNode(0)

            # 若达到l1的末尾， 则只计算l2
            if not l1:
                sum_ = l2.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l2 = l2.next

            # 若达到l2的末尾， 则只计算l1
            elif not l2:
                sum_ = l1.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l1 = l1.next

            else:
                # 设定结点最终值 x + y + carry
                sum_ = l1.val + l2.val + carry
                # 创建一个数值为sum_ % 10 的新节点， 并将其设置为
                # 当前节点的下一个节点，然后将当前节点前进到下一节点
                new_point.val = sum_ % 10
                carry = sum_ // 10

                # l1和l2 前进到下一个节点
                l1 = l1.next
                l2 = l2.next

            point.next = new_point
            point = point.next

        # 检查carry = 1, 是否成立， 如果成立
        # 则向返回列表追加一个含有数字1的新结点
        if carry:
            new_point = ListNode(1)
            point.next = new_point
        return head.next

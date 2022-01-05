class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = []

    def push(self, x: int):
        if not self.s1:
            # 把s1中压入的第一个元素赋值
            self.front = x
        # 新元素总是压入栈顶
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                # 把所有的s1中的元素弹出来并存入到s2中
                self.s2.append(self.s1.pop())
            self.front = None
        # s1中栈底的元素变成s2栈顶的元素， 可以直接弹出来
        return self.s2.pop()

    def peek(self):
        # 如果s2不为空， 直接返回s2的栈顶元素
        if self.s2:
            return self.s2[-1]
        # 否则返回赋值的front
        return self.front

    def empty(self):
        # 如果s1和s2都为空，True, 否则， False
        if not self.s1 and not self.s2:
            return True
        return False


s = MyQueue()
print(s.empty())
s.push(2)
print(s.empty())
s.push("dog")
print(s.peek())
s.pop()
print(s.peek())

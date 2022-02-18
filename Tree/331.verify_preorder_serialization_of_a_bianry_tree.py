"""
先判断【左子树】是否有效， 然后在判断【右子树】是否有效， 最后判断【根节点 - 左子树 - 右子树】是否有效。
这个思路类似于递归， 而把递归改成循环时， 就是使用【栈】
"""


def isValidSerialization(preorder):
    stack = []
    for node in preorder.split(""):
        stack.append(node)
        while len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[-3] != "#":
            stack.pop(), stack.pop(), stack.pop()
            stack.append("#")
    return len(stack) == 1 and stack.pop() == "#"


"""
Method 2: 计算出度和入度
"""


def isValidSerialization(preorder):
    # 计算出度和入度
    nodes = preorder.split("")
    diff = 1
    for node in nodes:
        diff -= 1
        if diff < 0:
            return False
        if node != "#":
            diff += 2
    return diff == 0
class Solution:
    def removeOuterparentheses(self, s: str) -> str:
        stack = []
        res = ""

        for i in range(len(s)):
            # 左括号入栈
            if s[i] == "(":
                # 入栈的是s的下标
                stack.append(i)
            # 右括号弹出栈顶
            else:
                left = stack.pop()
                # 判断是否为空
                if not stack:
                    # 获取栈顶index以及当前循环的下标i
                    res += s[left + 1 : i]

        return res


x = Solution()
print(x.removeOuterparentheses("((()))(())(((())))"))

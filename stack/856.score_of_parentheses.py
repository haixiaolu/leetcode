# 栈的深度， 栈的深度得分


class Solution:
    def scoreOfParentheses(self, S):

        stack = [0]
        for char in S:
            if char == "(":
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] = max(2 * score, 1)

        # 这里为什么要pop呢
        return stack.pop()


x = Solution()
print(x.scoreOfParentheses(S="(())"))

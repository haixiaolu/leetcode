class Solution:
    def isValid(self, s: str):
        if len(s) % 2 == 1:
            return False

        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in pairs:
                # 如果没有左括号， 或者不是相同的类型
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

            else:
                stack.append(char)

        return not stack


x = Solution()
print(x.isValid(s="(){}"))

# 遇到 +, - 先计算， 遇到(, 进栈， 遇到 )， 出栈， 变量， res, num, sign
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)

            elif char == "+" or char == "-":
                res += sign * num
                num = 0
                sign = 1 if char == "+" else -1

            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif char == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res


obj = Solution()
print(obj.calculate("1+1"))

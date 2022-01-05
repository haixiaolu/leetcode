class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # 记录插入次数
        res = 0
        # right_need 变量记录右括号的需求量
        right_need = 0

        for i in range(len(s)):
            if s[i] == "(":
                # 对右括号的需求+1
                right_need += 1

            elif s[i] == ")":
                # 对右括号的需求-1
                right_need -= 1
                if right_need == -1:
                    right_need = 0
                    # 需插入一个左括号
                    res += 1

        return res + right_need


x = Solution()
print(x.minAddToMakeValid(s="((()"))

# 和678的题思路一样
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        left = []
        star = []

        for i in range(n):
            if s[i] == "(" and locked[i] == "1":
                left.append(i)
            else:
                if locked[i] == "0":
                    star.append(i)
                else:
                    if left:
                        left.pop()
                    else:
                        if star:
                            star.pop()
                        else:
                            return False

        while left and star:
            if left[-1] <= star[-1]:
                left.pop()
                star.pop()
            else:
                return False

        return len(left) == 0 and len(star) % 2 == 0


obj = Solution()
print(obj.canBeValid(s="))()))", locked="010100"))

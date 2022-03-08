"""
中心拓展
- we choose all possible centers for potential palindromes
  - every single character in the string is a center for possible odd-length palindromes
  - every pair of consecutive characters in the string is a center for possible even-length palindromes
- For every center, we can expand around it as long as we get palindromes (the first and last characters match)
"""


class Solution:
    def contSubstrings(self, s):
        # 以每个位置作为回文中心， 尝试扩展
        # 回文中心有2种形式， 1个数或者2个数
        n = len(s)

        def spread(left, right):
            nonlocal ans
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1

        ans = 0
        for i in range(n):
            spread(i, i)
            spread(i, i + 1)
        return ans


s = Solution()
print(s.contSubstrings("abc"))
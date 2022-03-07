"""
1. 回文串的本质：
    除了中心字符外，其他字符都是偶数次
2. 最长回文串的构成：
    使所有字母尽可能多的出现偶数次 + 1次（此时如果还有字母没有用完）【需要统计每个字母的出现次数】
3. 最终思路：
    以字母的ASCII
"""
"""
哈希表：
    - 回文只需要偶数个字符串
    - 对最大偶数分别求和， 如果为奇数-1
    - 最后的值，需要判断原始的字符里面如果是奇数， 可以将字符放在中间， 并返回res + 1, 否则res
"""
import collections


class Solution:
    def longestPalindrome(self, s):
        res = []
        has_odd = False
        alp_map = collections.Counter(s)
        # print(alp_map)
        for _, num in alp_map.items():
            # print(num)
            if num % 2 == 0:
                res += num
            else:
                res += num - 1
                has_odd = True
        return res + 1 if has_odd else res


s = Solution()
print(s.longestPalindrome("abccccdd"))
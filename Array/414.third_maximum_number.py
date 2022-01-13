# brute force
# class Solution:
#     def thirdMax(self, nums):
#         nums.sort(reverse=True)
#         diff = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 diff += 1
#                 if diff == 3:
#                     return nums[i]
#         return nums[0]  # 返回最大的数， 如果没有第三位


# sortedList
# from sortedcontainers import SortedList

# class Solution:
#     def thirdMax(self, nums):
#         s = SortedList()
#         for num in nums:
#             if num not in s:
#                 s.add(num)
#                 # 如果长度比3大
#                 if len(s) > 3:
#                     s.pop()
#         return s[0] if len(s) == 3 else s[-1]

# 一次遍历
class Solution:
    def thirdMax(self, nums):
        a, b, c = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif a > num > b:
                b, c, = (
                    num,
                    b,
                )
            elif b > num > c:
                c = num
        return a if c == float("-inf") else c


o = Solution()
print(o.thirdMax([1, 3, 4, 5]))
print(o.thirdMax([1, 2]))
print(o.thirdMax([0]))

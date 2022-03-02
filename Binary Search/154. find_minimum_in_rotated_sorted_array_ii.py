"""
Tradition Binary Search with three cases:
1. nums[mid] < nums[right]
    - right = mid 
2. nums[mid] > nums[right]
    - left = mid + 1
3. nums[mid] == nums[right]
    - right = mid - 1
"""


from re import S


class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # case 1
            if nums[mid] < nums[right]:
                right = mid
                # should be right = right - 1
                # but its too aggressive to move the 'high' index
                # it won't work for the test case [3,1,3]
            # case 2
            elif nums[mid] > nums[right]:
                left = mid + 1
            # case 3
            right -= 1

        # the 'left' and 'right' index converge to the inflextion point
        return nums[left]


s = Solution()
print(s.findMin([1, 3, 5, 5, 1, 0]))
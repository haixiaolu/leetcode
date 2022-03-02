"""
The idea is that we add some additional condition checks in the normal binary search
- Initiate the pointer left to 0, right to n - 1
- perform standard binary search while left <= right
   - Take an index in the middle mid as a pivot
   - if nums[mid] == target, return mid 
   - Now these could be two situations:
        - nums[mid] > nums[left]
        - nums[mid] < nums[left]
"""


class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # case 1, 中间的大于左边的数， 没有旋转， 或者在旋转的一部分中
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        # case 2, 中间的小于右边的数， 没有旋转， 或者在旋转的一部分中


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))

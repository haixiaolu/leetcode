class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # leftBiased[True/False], if True, left is biased, if False, right is biased
    def binSearch(self, nums, target, leftBiased):
        left, right = 0, len(nums) - 1

        i = -1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                i = mid
                if leftBiased:
                    right = mid - 1
                else:
                    left = mid + 1
        return i

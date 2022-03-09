"""
1. Three pointers
   - use three pointers to track the rightmost boundary of zero, the leftmost boundary of twos and the current 
   element under the consideration

   - The idea of solution is to move curr pointer along the array. 
      - if nums[curr] == 0, swap it with nums[p0] 
      - if nums[curr] == 2, swap it with nums[p2]
"""


def sortColors(self, nums):
    # for all idx < p0: nums[idx < p0] = 0
    # curr is an index of element under consideration
    p0 = curr = 0
    # for all idx > p2: nums[idx > p2] = 2
    p2 = len(nums) - 1

    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[p2], nums[curr] = nums[curr], nums[p2]
            p2 -= 1
        else:
            curr += 1
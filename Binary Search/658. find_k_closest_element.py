"""
- Initialize two variables to perform binary search: left = 0 and right = len(arr) - k 
- Perfrom a binary search, at each operation, calculate `mid = (left + right) // 2` and compare the two element at 
    arr[mid + k] is close to x, then move the left pointer. remember, the smaller element always wins when there is tie
- At the end of the binary search, we have located the leftmost index for the final answer. Return the subarray starting at this index 
  that contains k elements
"""

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]


s = Solution()
print(s.findClosestElements([1, 2, 3, 4, 5], 4, 3))

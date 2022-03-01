"""
1. Split into two subproblems
    - define boundaries
       - initiate left = 0, and right = 1
       - while target is on the right to the right boundary: reader.get(right) < target
         - set left boundary equal to the right one: left = right
         - extend right boundary: right = right * 2
       - now the target is between left and right
    - binary search operation
"""


class ArrayReader:
    def get(self, index: int) -> int:
        pass


class Solution:
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0

        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right *= 2
        # binary search
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
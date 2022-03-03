"""
two helper functions:
    1. find the element in the row
    2. find the element in the column
then search top, bottom, left, right
"""
from numpy import searchsorted


class Solution:
    def minArea(self, image, x, y):
        top = self.searchRows(image, 0, x, True)
        bottom = self.searchRows(image, x + 1, len(image), False)
        left = self.searchColumns(image, 0, y, True, bottom, True)
        right = self.searchColumns(image, y + 1, len(image[0]), False, bottom, False)
        return (right - left) * (bottom - top)

    def searchRows(self, image, left, right, opt):
        while left != right:
            mid = (left + right) // 2
            if ("1" in image[mid]) == opt:
                right = mid
            else:
                left = mid + 1
        return left

    def searchColumns(self, image, left, right, opt, bottom, top):
        while left != right:
            mid = (left + right) // 2
            if any(image[k][mid] == "1" for k in range(bottom)) == opt:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
print(s.minArea(["0010", "0110", "0100", "0110"], 0, 2))
"""
1. Three pointers
    - set p1 to point at index m - 1 of nums1
    - p2 to point at index n - 1 of nums2
    and p to point at index m + n - 1 of nums1, this way it is guaranteed that once we start overwriting the first
    m values in nums1, we will have already written each into its new position. it can eliminate the additional space
"""


def merge(nums1, m, nums2, n):
    # set p1 and p2 to point the end of their respective arrays
    p1 = m - 1
    p2 = n - 1

    # add move p backwards through the array, each time writing
    # the smallest value pointed at by p1 or p2
    for p in range(n + m - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
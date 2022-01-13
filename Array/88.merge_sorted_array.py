class Solution:
    def merge(self, nums1, m, nums2, n):
        # last index nums1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and m > 0:
            # find largest value
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]  # replace last position in nums1
                m -= 1  # move nums1's pointer

            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1  # move combined array's pointer

        # edge case, if the first element in nums1 is larger than the first element of nums2
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1


obj = Solution()
print(obj.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

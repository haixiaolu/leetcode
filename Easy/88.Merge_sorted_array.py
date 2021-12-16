"""
Question: given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
          representing the number of elements in nums1 and nums 2 respectively

          Merge nums1 and nums2 into a single array sorted in non-decreasing order

          Do not return anything, modify nums1 in-place instead

          Input: nums1 = [1, 2, 3, 0, 0, 0] m = 3, nums2 = [ 2, 5, 6] n = 3 
"""
"""
Approach: 1. 直接合并和排序
            先将数组num2放进数组nums1的尾部， 然后直接对这个数组进行排序
          2. 双指针
          方法一没有利用数组nums1与nums2已经被排序的性质，可以利用双指针来实现
          - 两个数组看作队列， 每次从两个数组头部取出比较小的数字放到结果中，
          3. 逆向双指针
            方法二中之所以要使用临时变量，是因为如果直接合并到数组nums1中，nums1中的元素可能会在取出之前被覆盖
            为了避免被覆盖，nums1的后半部分是空的， 可以直接覆盖而不会影响结果， 因此可以指针设置从后向前遍历， 每次取两者之中的较大者放入nums1的最后面
"""

# 方法一： 直接合并后排序
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()


# Time: O((m + n)log(m + n)), 排序序列长度为m + n
# Space: O(log(m + n))

# 方法二：双指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sorted = []
        p1, p2 = 0, 0
        # 注意点： 必须当两个数组的指针都到达尾部时， 算法才算结束
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        # 对nums1从头到尾切片， 然后一一进行赋值， 相当于进行了深层拷贝
        nums1[:] = sorted


# Time: O(m + n)
# Space: O(m + n)

# 方法三： 逆向双指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


# Time: O(m + n)
# Space: O(1)

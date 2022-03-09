class Solution:
    def sortArray(self, nums):
        def choose_pivot(left, right):
            # pick 3 random numbers within the range of the list
            i1 = left + random.randint(0, right - left)
            i2 = left + random.randint(0, right - left)
            i3 = left + random.randint(0, right - left)

            # return their median
            return max(min(i1, i2), min(max(i1, i2), i3))

        def partition(lst, left, right):
            pivot_index = choose_pivot(left, right)  # index of pivot
            lst[right], lst[pivot_index] = (
                lst[pivot_index],
                lst[right],
            )  # put the pivot at the end
            pivot = lst[right]  # pivot
            i = (
                left - 1
            )  # all the elements less than or equal to the pivot go before or at i

            for j in range(left, right):
                if lst[j] <= pivot:
                    i += 1  # increment the index
                    lst[i], lst[j] = lst[j], lst[i]
            lst[i + 1], lst[right] = (
                lst[right],
                lst[i + 1],
            )  # puttting the pivot back in place
            return i + 1

        def quick_sort(lst, left, right):
            if left < right:
                # pi is where the pivot is at
                pi = partition(lst, left, right)
                # separately sort elements before and after partition
                quick_sort(lst, left, pi - 1)
                quick_sort(lst, pi + 1, right)

        quick_sort(nums, 0, len(nums) - 1)
        return nums

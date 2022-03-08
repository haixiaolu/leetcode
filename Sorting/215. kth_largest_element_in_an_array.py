"""
1. Quickselect
   The approach is basically the same as for quicksort, notice the Kth largest element is the same as (N - k)th smallest element.
   Hence one could implement kth smallest algorithm for this problem
Algorithm:
    1. choose a random pivot
    2. use a partition algorithm to place the pivot into its perfect position pos in the sorted array, 
       move smaller element to the left of pivot, and larger or equal ones, to the right 
    3. compare pos and n-k to choose the side of array to proceed recursively 
"""


def findKthLargest(nums, k):
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def select(left, right, k_smallest):
        """
        Returns the k-th smallest element of list within left..right
        """
        if left == right:  # if the list contains only one element, return that element
            return nums[left]

        # select a random pivot_index between
        pivot_index = random.randint(left, right)

        # find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]

        # go left
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)

        # go right
        else:
            return select(pivot_index + 1, right, k_smallest)

    # kth largest is (n-k)th smallest
    return select(0, len(nums) - 1, len(nums) - k)

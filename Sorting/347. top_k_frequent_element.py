"""
1. QuickSelect 
 - build a hashmap element -> frequency and convert its key into the array unique of unique element. 
    - Note that elements are unique, but their frequencies are not. That means we need a partition algorithm that works fine
      with duplicates 
 - work with unqiue array. Use a partition scheme to place the pivot into its perfect position pivot index in the sorted 
   array, move less frequent elements to the left of pivot, and more frequent or of the same frequency - to the right
 - compare pivot_index and N - k
    - if pivot_index == N - k, the pivot is N - kth most frequent element, and all elements on the right are more 
      frequent or of the same frequency. Return these top k frequent elements 
    - otherwise, choose the side of the array to proceed recursively 
"""


class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            # 1.move pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move less frequent elements to the left of pivot
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]
            return store_index

        def quickselect(left, right, k_smallest):
            # base case: the list contains only one element
            if left == right:
                return nums[left]

            # select a random pivot_index
            pivot_index = random.randint(left, right)
            # find the pivot position in a sorted array
            pivot_index = partition(left, right, pivot_index)
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return

            # go left
            elif k_smallest < pivot_index:
                self.quickselect(left, pivot_index - 1, k_smallest)

            # go right
            else:
                self.quickselect(pivot_index + 1, right, k_smallest)

        n = len(nums)
        # kth top frequent element is (n - k)th less frequent element
        # do a partial sort: from less frequent to the msot frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array
        # all element on the left are less frequent
        # all element on the right are more frequent or of the same frequency
        self.quickselect(0, n - 1, n - k)
        # return the top k frequent elements
        return unique[n - k :]

import heapq


class Solution:
    def medianSlidingWindow(self, nums, k):
        self.maxHeap = []
        self.minHeap = []

        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -nums[i])
            else:
                heapq.heappush(self.minHeap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 > 0:  # if we have at least 'k' elements in the sliding window
                # add the median to the result array
                result[i - k + 1] = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
            else:  # because max heap will have one more element than min heap
                result[i - k + 1] = -self.maxHeap / 1.0

            # remove the element going out of the sliding window
            elementToBeRemoved = nums[i - k + 1]
            if elementToBeRemoved <= -self.maxHeap[0]:
                self.remove(self.maxHeap, -elementToBeRemoved)
            else:
                self.remove(self.minHeap, elementToBeRemoved)

            self.rebalance_heaps()
        return result

    # removes an element from the heap keeping the heap property
    def remove(self, heap, element):
        ind = heap.index(element)  # find the element
        # move the element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]
        # we can use heapify to readjust the elements but that would be O(n)
        # instead, we will adjust only one element which will O(logN)
        if ind < len(heap):
            ind = heap.index(element)
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

    def rebalance_heaps(self):
        # either both the heaps will have equal number of elements or max-heap will have
        # one more element that the min heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

"""
divide the list into two parts
- one half to store all the smaller number
- another half to store all the larger number
- the median of all the number will either be the larger number 
    in the smaller part or smaller number in larger part

--> We can store the first half in Max Heap as we want the largest
--> store the second half in Min Heap as we want the smallest
--> At any time, the median of the current list of numbers can be calculated from the top element of the two heaps
"""
import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.maxHeap = []  # containing first half of numbers
        self.minHeap = []  # containing second half of number

    def addNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.eappush(self.minHeap, num)

        # either both the heap will have equal number of elements or max-heap will have
        # one more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            # we have even number of elements, take the average of middle two number
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        else:
            return -self.maxHeap[0] / 1.0


s = MedianFinder()
s.addNum(2)
s.addNum(1)
print(s.findMedian())

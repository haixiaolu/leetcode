"""
- build a hashMap use dictionary to initialize the hashMap
- build a heap of size k using N elements.
- last is to convert the heap into an output array
"""
import collections
import heapq
from typing import Counter


def topFrequent(nums, k):
    if k == len(nums):
        return nums

    # build hashmap
    count = Counter(nums)

    # 2-3, build heap with top k
    return heapq.nlargest(k, count.keys(), key=count.key)


# O(N) Solution
# Bucket Sort
"""
- create list of empty lists for buckets
- use Counter to count frequencies of elements in nums
- Iterate over our Counter and add elements to corresponding buckets
- buckets is list of lists now, create one big list out of it
- Finally, take the k last elements from this list, these elements will be top k frequent elements
"""


def topKFrequent(nums, k):
    buckets = [[] for _ in range(len(nums) + 1)]
    number_count = collections.defaultdict(int)
    for num in nums:
        number_count[num] += 1

    for num, freq in number_count.items():
        buckets[freq].append(num)

    # buckets is a double array
    flat_list = []
    # traverse from right to left so number with higher frequency come first
    for i in range(len(buckets) - 1, -1, -1):
        bucket = buckets[i]
        if bucket:
            for num in bucket:
                flat_list.append(num)
    return flat_list[:k]
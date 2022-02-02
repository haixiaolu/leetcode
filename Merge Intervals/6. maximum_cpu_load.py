# leetcode, discussion: Find Max Bandwidth
"""
Given a list of jobs, each job has a Start time, an End time, and a CPU load when it is running.
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine. 
"""
"""
Similar to "Minimum Meeting Rooms" where we were trying to find the maximum number of meetings happening at 
any time, For 
"""
from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on job.end
        return self.end < other.end

    def find_max_cpu_load(jobs):
        # sort the jobs by start time
        jobs.sort(key=lambda x: x.start)
        max_cpu_load, current_cpu_load = 0, 0
        min_heap = []
        for j in jobs:
            # remove all the jobs that have ended
            while len(min_heap) > 0 and j.start >= min_heap[0].end:
                current_cpu_load -= min_heap[0].cpu_load
                heappop(min_heap)
            # add the current job into min_heap
            heappush(min_heap, j)
            current_cpu_load += j.cpu_load
            max_cpu_load = max(max_cpu_load, current_cpu_load)
        return max_cpu_load

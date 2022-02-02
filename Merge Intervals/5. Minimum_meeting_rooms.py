# leetcode 253. Meeting rooms II
"""
Given a list of intervals representing the start and end time of 'N' meetings, find the minimum number of rooms
required to hold all the meetings
"""
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end

    def min_meeting_rooms(self, meetings):
        meetings.sort(key=lambda x: x.start)
        minRooms = 0
        minHeap = []
        for meeting in meetings:
            while len(minHeap) > 0 and meeting.start >= minHeap[0].end:
                heappop(minHeap)

            heappush(minHeap, meeting)
            minRooms = max(minRooms, len(minHeap))
        return minRooms

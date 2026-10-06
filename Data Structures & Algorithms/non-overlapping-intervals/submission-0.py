class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        removals = 0
        end = float("-inf")

        for start, finish in intervals:
            if start >= end:
                end = finish
            else:
                removals += 1

        return removals

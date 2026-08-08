class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval : interval[0])
        previous_end = intervals[0][1]
        n = len(intervals)
        count = 0

        for i in range(1, n):
            if previous_end <= intervals[i][0]:
                previous_end = intervals[i][1]
            else:
                previous_end = min(previous_end, intervals[i][1])
                count += 1
        
        return count
        

                
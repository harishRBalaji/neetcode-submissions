class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval : interval[0])
        output = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            if output[-1][1] < intervals[i][0]:
                output.append(intervals[i])
            else:
                output[-1][1] = max(output[-1][1], intervals[i][1])
        return output

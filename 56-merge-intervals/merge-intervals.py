class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if end >= intervals[i][0]:
                start = start
                end = max(end,intervals[i][1])
                continue
            s.append([start,end])
            start = intervals[i][0]
            end = intervals[i][1]
        s.append([start,end])
        return s
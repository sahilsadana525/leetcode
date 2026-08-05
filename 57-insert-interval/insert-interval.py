class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        k = 0
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        for i in range(len(intervals)):
            if intervals[i][0] <=  newInterval[0]:
                k+=1
        intervals.insert(k,newInterval)
        start1 = intervals[0][0]
        end1 = intervals[0][1]
        for i in range(len(intervals)):
            if end1 >= intervals[i][0]:
                start1 = start1
                end1 = max(end1,intervals[i][1])
                continue
            res.append([start1,end1])
            start1 = intervals[i][0]
            end1 = intervals[i][1]
        res.append([start1,end1])
        return res
            
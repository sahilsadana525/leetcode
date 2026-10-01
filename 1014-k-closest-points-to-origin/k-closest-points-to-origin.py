import heapq
class Pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def __lt__(self,other):
        if self.first != other.first:
            return self.first > other.first
        return self.second > other.second
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        res = []
        for i in range(k):
            d = points[i][0]**2+points[i][1]**2
            heapq.heappush(heap,Pair(d,points[i]))
        for i in range(k,len(points)):
            d = points[i][0]**2+points[i][1]**2
            if d > heap[0].first:
                continue
            p = heapq.heappop(heap)
            heapq.heappush(heap,Pair(d,points[i]))
        while heap:
            res.append(heapq.heappop(heap).second)
        return res


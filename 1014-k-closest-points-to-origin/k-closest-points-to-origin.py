import heapq
class Pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def __lt__(self,other):
        if self.first != other.first:
            return self.first< other.first
        return self.second< other.second
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        res = []
        for i in range(len(points)):
            d = sqrt(points[i][0]**2+points[i][1]**2)
            heapq.heappush(heap,Pair(d,points[i]))
        while k!=0:
            p = heapq.heappop(heap)
            res.append(p.second)
            k-=1
        return res


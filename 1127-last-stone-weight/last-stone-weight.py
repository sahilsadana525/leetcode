import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap,-stones[i])
        while heap:
            if len(heap) == 1:
                return -heap[-1]
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x == y:
                continue
            elif x!=y:
                heapq.heappush(heap,(y-x))
        if len(heap) == 0:
            return 0
        else:
            return -heap[-1]



        
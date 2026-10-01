import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        proj = []
        n = len(capital)
        for i in range(n):
            proj.append([capital[i],profits[i]])
        proj.sort()
        h = []
        idx = 0
        while k!=0:
            while idx < n:
                if proj[idx][0] > w:
                    break
                heapq.heappush(h,-proj[idx][1])
                idx+=1
            if not h:
                return w
            w = w + (-heapq.heappop(h))
            k-=1
        return w
            


        
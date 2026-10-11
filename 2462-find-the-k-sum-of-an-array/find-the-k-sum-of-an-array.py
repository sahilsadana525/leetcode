import heapq
class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        max_sum = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                max_sum+=nums[i]
            else:
                continue
        l = []
        heap = []
        l = sorted(abs(x) for x in nums) 
        heapq.heappush(heap,(0,-1))
        loss = 0 
        for _ in range(k):
            loss,i = heapq.heappop(heap)

            if i == -1:
                heapq.heappush(heap,(l[0],0))
                continue

            if i + 1 < len(l):
                new_loss = loss - l[i] + l[i+1]
                heapq.heappush(heap,(new_loss,i+1))

                new_loss = loss + l[i+1]
                heapq.heappush(heap,(new_loss,i+1))

        return max_sum - loss

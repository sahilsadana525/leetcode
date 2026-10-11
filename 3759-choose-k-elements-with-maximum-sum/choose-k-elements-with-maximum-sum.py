class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
            n = len(nums1)
            heap = []
            total = 0
            ans = [0]*n
            i = 0
            indices = sorted(range(len(nums1)), key=lambda i: nums1[i])
            while i < n:
                j = i
                while j < n and nums1[indices[j]] == nums1[indices[i]]:
                    j += 1
        
                for p in range(i,j):
                    idx = indices[p]
                    ans[idx] = total
        
                for p in range(i,j):
                    idx = indices[p]
                    heapq.heappush(heap,nums2[idx])
                    total += nums2[idx]
            
                    if len(heap) > k:
                        total -= heapq.heappop(heap)
                i = j       
            return ans 
    
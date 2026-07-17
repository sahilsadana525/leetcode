from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        max_sum = 0
        window_sum = 0
        for i in range(len(nums)):
            freq[nums[i]]+=1
            window_sum += nums[i]
            if i>=k:
                freq[nums[i-k]]-=1
                window_sum-=nums[i-k]
                if freq[nums[i-k]]==0:
                    del freq[nums[i-k]]
            if i >= k-1 and len(freq) == k:
                max_sum = max(max_sum,window_sum)
        return max_sum



                

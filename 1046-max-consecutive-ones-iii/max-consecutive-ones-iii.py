from collections import defaultdict
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = 0
        res = float('-inf')
        c = defaultdict(int)
        for high in range(len(nums)):
            c[nums[high]] += 1
            len1 = high - low + 1 
            diff = len1 - c[1]
            while diff > k:
                c[nums[low]]-=1
                low +=1
                len1 = high - low + 1
                diff = len1 - c[1]
            len1 = high - low + 1
            res = max(res,len1)
        return res

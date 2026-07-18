class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        res = float('inf')
        s = 0
        while high < len(nums):
            s = s + nums[high]
            while s >= target:
                window = high - low + 1
                res = min(res,window)
                s  = s - nums[low]
                low+=1
            high+=1
        if res == float('inf'):
            return 0
        else:
            return res
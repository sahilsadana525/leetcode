class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k) - self.atmost(nums,k-1)
    def atmost(self,nums,k):
        high, low = 0,0
        sum1 = 0
        res = 0
        if k < 0:
            return 0
        while high < len(nums):
            sum1 = sum1 + (nums[high]%2)
            while sum1 > k:
                sum1 = sum1 - (nums[low]%2)
                low+=1
            res = res + (high - low + 1)
            high+=1
        return res

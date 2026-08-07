class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atmost(nums,goal) - self.atmost(nums,goal-1)
    def atmost(self,nums,goal):
        h,l = 0,0
        sum1 = 0
        res = 0
        if goal < 0:
            return 0
        while h < len(nums):
            sum1+=nums[h]
            while sum1 > goal:
                sum1-=nums[l]
                l+=1
            res = res + (h-l+1)
            h = h+1
        return res
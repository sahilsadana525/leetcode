class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ending = nums[0]
        min_ending = nums[0]
        ans = nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = nums[i]*max_ending
            v3 = nums[i]*min_ending
            max_ending = max(v1,max(v2,v3))
            min_ending = min(v1,min(v2,v3))
            ans = max(ans,max_ending)
        return ans
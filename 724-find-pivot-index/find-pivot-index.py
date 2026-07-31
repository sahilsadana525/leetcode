class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        suff = 0
        s = sum(nums)
        for i in range(0,len(nums)):
            if i != 0:
                prefix+=nums[i-1]
            suff = s - (nums[i] + prefix)
            if suff == prefix:
                return i
        return -1
    
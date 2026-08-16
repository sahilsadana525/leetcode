from typing import List
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        for i in range(len(nums)):
            if abs(nums[i]-i)>1:
                return False
        return True

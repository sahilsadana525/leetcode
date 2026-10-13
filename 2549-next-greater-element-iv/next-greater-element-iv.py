class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1]*n
        s1 = []
        s2 = []
        for i in range(n):
            while s2 and nums[s2[-1]] < nums[i]:
                res[s2.pop()] = nums[i]
            temp = []
            while s1 and nums[s1[-1]] < nums[i]:
                temp.append(s1.pop())
            while temp:
                s2.append(temp.pop())
            s1.append(i)
        return res




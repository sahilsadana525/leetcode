from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        f = defaultdict(int)
        s = 0
        res = 0
        f[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            rem = s % k
            if rem < 0:
                rem = rem + k
            res+=f[rem]
            f[rem]+=1
        return res
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        f = defaultdict(int)
        s = 0
        f[0]=1
        res = 0
        for i in range(len(nums)):
            s+=nums[i]
            ques = s - k
            freq = f[ques]
            res += freq
            f[s]+=1
        return res

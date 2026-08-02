from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        f = defaultdict(int)
        zero = 0
        one = 0
        res = 0
        len1 = float('-inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                zero+=1
            else:
                one+=1
            diff = zero - one
            if diff == 0:
                res = max(res,i+1)
                continue
            if diff not in f:
                f[diff] = i
            else:
                ixd = f[diff]
                len1 = i - ixd
                res = max(res,len1)
        return res


        
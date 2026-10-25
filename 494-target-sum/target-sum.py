class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        sum1 = sum(nums)
        if sum1 < abs(target) or (sum1 + target) % 2 != 0:
            return 0
        s1 = (target + sum1)//2 

        dp = [[0]*(s1+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(s1+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][s1]
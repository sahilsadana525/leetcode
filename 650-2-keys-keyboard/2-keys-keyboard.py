class Solution:
    def minSteps(self, n: int) -> int:
        ans = float('inf')
        p = 0
        dp = [-1]*(n+1)
        if n == 1:
            return 0 
        if dp[n]!=-1:
            return dp[i]
        
        for i in range(1,n):
            if n % i == 0:
                p = self.minSteps(i) + n//i
                ans = min(ans,p)
        dp[n] = ans

        return ans        

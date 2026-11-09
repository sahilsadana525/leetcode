class Solution:
    def minCut(self, s: str) -> int:
        dp = [[-1] * (len(s)+1) for i in range(len(s)+1)]
        return self.solve(s, 0, len(s)-1,dp)

    def solve(self, s, i, j,dp):

        if i >= j:
            return 0

        if s[i:j+1] == s[i:j+1][::-1]:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
    

        mn = float('inf')

        for k in range(i, j):

            if s[i:k+1] == s[i:k+1][::-1]:

                temp = 1 + self.solve(s, k+1, j,dp)

                mn = min(mn, temp)
        dp[i][j] = mn

        return dp[i][j]
           
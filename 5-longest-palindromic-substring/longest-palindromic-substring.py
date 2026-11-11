class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1 = s[::-1]
        n = len(s)
        mn = 0
        L = 0
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == s1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                L = dp[i][j]
                if L > 0 and i - L == n - j:
                    if L > mn:
                        mn = L
                        start = i - L
        return s[start:start+mn]
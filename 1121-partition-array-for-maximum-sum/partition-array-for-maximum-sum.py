class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        sum1 = 0
        for i in range(n-1,-1,-1):
            maxi = float('-inf')
            max_ans = float('-inf')
            len1= 0
            for j in range(i,min(n,i+k)):
                len1+=1
                maxi = max(maxi,arr[j])
                sum1 = (len1 * maxi) + dp[j+1]
                max_ans = max(max_ans,sum1)
            dp[i] = max_ans
        return dp[0]

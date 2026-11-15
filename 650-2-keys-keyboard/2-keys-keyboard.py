class Solution:
    def minSteps(self, n: int) -> int:
        ans = float('inf')
        p = 0
        if n == 1:
            return 0
        
        for i in range(1,n):
            if n % i == 0:
                p = self.minSteps(i) + n//i
                ans = min(ans,p)

        return ans        

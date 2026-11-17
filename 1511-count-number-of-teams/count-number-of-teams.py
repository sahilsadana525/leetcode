class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n= len(rating)
        inc = [0]*n
        dec = [0]*n 
        ans = 0 
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    inc[i]+=1
                    ans +=inc[j]
                elif rating[i] < rating[j]:
                    dec[i] +=1
                    ans +=dec[j]
        return ans      
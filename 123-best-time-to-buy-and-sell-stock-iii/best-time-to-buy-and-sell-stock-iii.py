class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        cur = [[0]*3 for _ in range(2)]
        next1 = [[0]*3 for _ in range(2)]

        for i in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy == 1:
                        cur[buy][cap] = max(-prices[i] + next1[0][cap],next1[1][cap])
                    else:
                        cur[buy][cap] = max(prices[i] + next1[1][cap-1],next1[0][cap])
            next1 = cur
        return next1[1][2]
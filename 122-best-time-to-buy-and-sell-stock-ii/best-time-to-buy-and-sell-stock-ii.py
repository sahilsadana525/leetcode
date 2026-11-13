class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ahead = [0,0]
        cur = [0,0]
        n = len(prices)
        for i in range(n-1,-1,-1):
            for buy in range(2):
                profit = 0
                if buy == 1:
                    profit = max(- prices[i] + ahead[0],ahead[1])
                else:
                    profit = max(prices[i] + ahead[1],ahead[0])
                cur[buy] = profit
            ahead = cur.copy()
        return ahead[1]
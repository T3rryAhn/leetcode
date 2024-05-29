class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            temp_profit = 0
            temp_profit = max(prices[i + 1:]) - prices[i]
        
            profit = max(profit, temp_profit)

        return profit

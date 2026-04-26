class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start = end = profit = maxProfit = 0

        while end < len(prices) and start < len(prices):
            if prices[end] - prices[start] >= 0:
                profit = prices[end] - prices[start]
                end += 1
                maxProfit = max(maxProfit, profit)
            
            else:
                start += 1
            
        
        return maxProfit

        
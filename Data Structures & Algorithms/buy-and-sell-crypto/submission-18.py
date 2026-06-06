class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start = end = maxProfit = 0

        while start < len(prices) and end < len(prices):
            temp = prices[end] - prices[start]

            if temp >= 0:
                end += 1
                maxProfit = max(maxProfit, temp)
            
            else:
                start += 1
        
        return maxProfit
        
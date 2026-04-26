class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = a = b = 0

        while a <= len(prices)-1 and b <= len(prices)-1:
            if prices[b] - prices[a] >= 0:
                if profit < prices[b]-prices[a]:
                    profit = prices[b]-prices[a]
                b = b+1
            else:
                a = a+1
        
        return profit

        
                    
        
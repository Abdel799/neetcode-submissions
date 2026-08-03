class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        slow = fast = maxProfit = 0
    
        while slow < len(prices) and fast < len(prices):
        
            if prices[fast] - prices[slow] >= 0:
                maxProfit = max(maxProfit,prices[fast] - prices[slow])
                fast += 1
        
            else:
                slow += 1
    
        return maxProfit
        
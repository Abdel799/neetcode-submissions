class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #basically we're looking for the biggest area

        maximum = 0

        for i in range (len(heights)):

            for j in range (i, len(heights)):
                
                small = min(heights[i], heights[j])
                maximum = max(small * (j-i), maximum)
        
        return maximum

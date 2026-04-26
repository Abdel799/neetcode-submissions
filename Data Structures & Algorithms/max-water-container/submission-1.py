class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #basically we're looking for the biggest area

        #maximum = 0

        #for i in range (len(heights)):

        #    for j in range (i, len(heights)):
                
        #        small = min(heights[i], heights[j])
        #        maximum = max(small * (j-i), maximum)
        
        #return maximum

        p1 = 0
        p2 = len(heights)-1
        maximum = 0

        while p1 < p2:

            small = min(heights[p1], heights[p2])
            maximum = max(small * (p2-p1), maximum)

            if small == heights[p1]:
                p1 = p1 + 1
            else:
                p2 = p2 - 1
        
        return maximum

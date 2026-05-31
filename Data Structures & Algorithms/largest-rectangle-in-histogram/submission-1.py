class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        maxArea = 0

        for index, height2 in enumerate(heights):
            start = index
            while s != [] and s[-1][1] > height2:
                i, h = s.pop()
                tempArea = h * (index - i)
                maxArea = max(maxArea, tempArea)
                start = i
            s.append((start, height2))
        
        for index, height2 in s:
            tempArea = height2 * (len(heights) - index)
            maxArea = max(maxArea, tempArea)
        
        return maxArea

        

        
        
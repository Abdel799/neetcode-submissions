class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        maxArea = 0

        for index, h in enumerate(height):

            while s and s[-1][1] < h:
                floorIndex, floor = s.pop()

                if not s:
                    break
                
                maxArea += (min(h, s[-1][1]) - floor) * (index - s[-1][0] - 1)
            s.append((index, h))
        
        return maxArea
        
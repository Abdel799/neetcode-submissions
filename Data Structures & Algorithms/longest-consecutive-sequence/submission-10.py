class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxCount = 0

        if nums == []:
            return 0
        
        stack = [nums[0]]
        
        for num in nums:

            if num == stack[-1]:
                continue
            
            elif num == stack[-1]+1:
                stack.append(num)

            else:
                maxCount = max(maxCount, len(stack))
                stack = [num]
            
        return max(maxCount, len(stack))
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return len(nums)
        
        p1= 1
        p2 = 1

        while p2 < len(nums):

            if nums[p2] == nums[p2-1]:
                p2 = p2 + 1
            
            else:
                nums[p1] = nums[p2]
                p1 = p1 + 1
                p2 = p2 + 1
        
        return p1
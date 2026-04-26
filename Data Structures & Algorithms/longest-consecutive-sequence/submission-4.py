class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # Bubble Sort
        # ----------------------------------
        for i in range (0,len(nums)):

            for j in range (0,len(nums)-1):

                if nums[j] > nums[j+1]:
                    temp=nums[j+1]
                    nums[j+1]=nums[j]
                    nums[j]=temp
        
        # ----------------------------------

        maxsub = 1
        sub = 1
        for i in range (0,len(nums)-1):

            if nums[i+1] == nums[i]+1:
                sub = sub + 1
            
            elif nums[i+1] == nums[i]:
                sub = sub

            else:
                maxsub = max(maxsub, sub)
                sub = 1

        maxsub = max(maxsub, sub)
        
        return maxsub


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # Bubble Sort: Keeps swapping adjacent pairs for n length of array times
        # ----------------------------------
       # for i in range (0,len(nums)):

         #   for j in range (0,len(nums)-1):

        #        if nums[j] > nums[j+1]:
        #            temp=nums[j+1]
        #            nums[j+1]=nums[j]
        #            nums[j]=temp
        
        # ----------------------------------

        # Selection Sort: Picks the current item, and compares it to entire array to find the lowest, then swap the current and the minIndex
        # ----------------------------------
        #for i in range(0,len(nums)):

           # minimum = nums[i]
           # minIndex = i
           # temp = 0

           # for j in range(i,len(nums)):
                
             #   if nums[j] < minimum:
            #        minimum = nums[j]
           #         minIndex = j
            
           # temp = nums[i]
           # nums[i] = minimum
           # nums[minIndex] = temp
        # ----------------------------------

        # Insertion Sort
        # ----------------------------------
        for i in range (0,len(nums)-1):
            current = nums[i+1]
            j=i
            index = i+1
            while j >= 0 and nums[j] > current:
                
                nums[j+1] = nums[j]
                index = j
                j = j - 1
            nums[index] = current
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


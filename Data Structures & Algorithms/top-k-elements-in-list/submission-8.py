class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        p = 0

        if nums == []:
            return []
        
        if len(nums) == 1:
            return nums
        
        # [1,2,3,4]
        maxNum = 1
        maxCount = 1
        while p < k:
        
            for i in range (0, len(nums)):

                count = 1
                current = nums[i]

                for j in range (i+1, len(nums)):

                    if nums[j] == current:
                        count = count + 1
                
                if count >= maxCount:
                    maxCount = count
                    maxNum = current

            if maxNum not in result:
                result.append(maxNum)
                nums = [x for x in nums if x != maxNum]


            maxCount=1
            
            p = p + 1

        return result

            
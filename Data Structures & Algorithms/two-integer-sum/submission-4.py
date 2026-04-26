class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = [0] * 2

        myMap = {}

        for i in range (0, len(nums)):
            temp = target - nums[i]

            if temp not in myMap:
                myMap[nums[i]] = i
            
            else:
                result[0] = myMap[temp]
                result[1] = i
                return result
        
        return result
        
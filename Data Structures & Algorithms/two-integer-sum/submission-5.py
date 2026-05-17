class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff not in seen:
                seen[value] = index
            
            else:
                return [seen[diff], index]
        
        return [0,0]
        
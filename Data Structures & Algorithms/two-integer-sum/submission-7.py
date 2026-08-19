class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if not diff in seen:
                seen[num] = i
            else:
                return [seen[diff], i]
        
        return [0,0]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        used = []
        extra = []

        for i in range(len(nums)):
            if nums[i] in used:
                extra.append(nums[i])
                continue
            
            used.append(nums[i])
        
        for i in extra:
            nums.remove(i)

        return len(nums)
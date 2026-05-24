class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        p = 1

        for i in range (len(nums)):
            
            for j in range (len(nums)):
                if i == j:
                    continue
                
                p *= nums[j]
            
            result.append(p)
            p=1

        return result
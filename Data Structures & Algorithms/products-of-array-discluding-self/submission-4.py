class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = []
        result = []

        product = 1

        # populating prefix array
        for num in nums:
            product *= num
            prefix.append(product)
        
        product = 1

        # populating suffix array
        i = len(nums)-1
        suffix = [1] * len(nums)
        while i >= 0:
            product *= nums[i]
            suffix[i] = product
            i -= 1
        
        # populating result array
        for i in range (len(nums)):
            if i != 0 and i != len(nums)-1:
                result.append(prefix[i-1] * suffix[i+1])
            elif i == 0:
                result.append(suffix[i+1])
            
            else:
                result.append(prefix[i-1])
            
        
        return result
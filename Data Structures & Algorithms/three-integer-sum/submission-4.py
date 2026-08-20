class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            p1 = i+1
            p2 = len(nums)-1

            while p1 < p2:

                if nums[p1] + nums[p2] == -num and [num, nums[p1], nums[p2]] not in result:
                    result.append([num, nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                
                elif nums[p1] + nums[p2] > -num:
                    p2 -= 1
                
                else:
                    p1 += 1
            
        return result
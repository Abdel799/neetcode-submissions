class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums.sort()
        i=0
        while i < len(nums)-1:

            p1 = i+1
            p2 = len(nums)-1

            while p1 < p2:

                if nums[p1] + nums[p2] == -(nums[i]) and [nums[i],nums[p1],nums[p2]] not in result:
                    result.append([nums[i],nums[p1],nums[p2]])
                    p1 = p1 + 1
                    p2 = p2 - 1
                
                elif nums[p1] + nums[p2] > -(nums[i]):
                    p2 = p2 - 1

                else:
                    p1 = p1 + 1
            i = i + 1
        
        return result


        
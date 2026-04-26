class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        used = []

        nums.sort()
        
        for i in range (len(nums)-1):
            p1 = i+1
            p2 = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while p1 < p2:

                if nums[p1] + nums[p2] == -nums[i]:
                    
                    result.append([nums[p1],nums[p2],nums[i]])
                    p1 = p1 + 1
                    p2 = p2 - 1

                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1

                    while p1 < p2 and nums[p2] == nums[p2+1]:
                        p2 -= 1

                elif nums[p1] + nums[p2] > -nums[i]:
                    p2 = p2 - 1

                else:
                    p1 = p1 + 1 

        return result               
        
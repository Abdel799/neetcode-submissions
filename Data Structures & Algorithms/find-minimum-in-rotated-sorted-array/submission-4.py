class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Explanation: 
        # Say we have [4, 5, 6, 7, 0, 1, 2]
        # The array is sorted from 4 - 7,
        # but the sorted pattern breaks when you see 0
        # This indicates thats where the rotation happened
        # So in this solution, we are looking for the half
        # That is out of order, because that's where the min will be.
        
        # In this case, mid = (0 + 6) // 2 = 3
        # nums[mid] = 7
        # By default we set res to be nums[0]
        # So far the smallest number is nums[0]
        # as indicated by res = min(res, nums[min])
        # if 7 > 4 that means the left half is sorted
        # and the right half is out of order
        # Therefore we need to look in the right half
        # So we set the left pointer to be mid + 1
        # and keep the right pointer as is.
        # We see that nums[l] < nums[r] (0 < 2)
        # Therefore 0 must be the answer
        # But to verify we do min(res, nums[l])
        # And we return res
        
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:

            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(nums[mid], res)

            if nums[l] <= nums[mid]:
                l = mid + 1
            
            else:
                r = mid - 1


        return res   

        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (r + l) // 2

            if nums[mid] == target:
                return mid

            # checking if left half is sorted
            if nums[mid] >= nums[l]:    
            
                # if sorted, check is target is in range
                if target >= nums[l] and target < nums[mid]:
                    r = mid-1
                
                else:
                    l = mid+1
            
            # right half is sorted
            else:
            
                # check range
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                
                else:
                    r = mid - 1

        return -1



        
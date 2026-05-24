class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for array in matrix:
            if self.binarySearch(array, target) == True:
                return True
            
        return False

    def binarySearch(self, array: List[int], target: int) -> bool:
        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (high + low) // 2

            if array[mid] == target:
                return True
            elif array[mid] > target:
                high = mid - 1
            elif array[mid] < target:
                low = mid + 1
            
        return False
        
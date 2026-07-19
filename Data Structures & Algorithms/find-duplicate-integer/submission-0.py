class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = []

        for n in nums:
            if n in temp:
                return n
            else:
                temp.append(n)
        
        return 0
        
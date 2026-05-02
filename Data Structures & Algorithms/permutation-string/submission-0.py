class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        start = 0
        end = len(s1)-1
        s = sorted(list(s1))
        temp = []

        while end < len(s2):

            for i in range (start,end+1):
                temp.append(s2[i])

            tempSort = sorted(temp)
            if tempSort == s:
                return True
            
            start += 1
            end += 1
            temp = []
        
        return False
        
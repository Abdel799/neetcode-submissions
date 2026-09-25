class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mySet = set()
        maxCount, count = 0,0
        p1, p2 = 0,0

        while p2 < len(s):
            
            if s[p2] not in mySet:
                mySet.add(s[p2])
                count += 1
                p2 += 1
            
            else:
                maxCount = max(maxCount, count)
                mySet.remove(s[p1])
                count -= 1
                p1 += 1
        
        return max(maxCount, count)
            
    

        
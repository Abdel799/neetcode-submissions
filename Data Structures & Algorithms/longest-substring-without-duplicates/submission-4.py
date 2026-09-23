class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = end = count = maxCount = 0
        mySet = set()

        while end < len(s) and start < len(s):
            if s[end] not in mySet:
                mySet.add(s[end])
                end += 1
                count += 1
                maxCount = max(maxCount, count)
            
            else:
                mySet.remove(s[start])
                start += 1
                count -= 1
        
        return maxCount

        
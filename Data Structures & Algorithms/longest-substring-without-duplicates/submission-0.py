class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = end = count = maxCount = 0
        stack = []

        while end < len(s) and start < len(s):
            if s[end] not in stack:
                stack.append(s[end])
                end += 1
                count += 1
                maxCount = max(maxCount, count)
            
            else:
                start += 1
                count -= 1
                stack.pop(0)
        
        return maxCount

        
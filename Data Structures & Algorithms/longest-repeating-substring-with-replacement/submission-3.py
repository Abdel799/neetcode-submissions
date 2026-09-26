class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        d = {}
        start = maxResult = 0

        for end in range (len(s)):

            char = s[end]
            d[char] = d.get(char,0) + 1

            while (end - start + 1) - max(d.values()) > k:
                char = s[start]
                d[char] -= 1

                if d[char] == 0:
                    d.pop(char)
                
                start += 1
            
            maxResult = max(end - start + 1, maxResult)
        
        return maxResult

        
        
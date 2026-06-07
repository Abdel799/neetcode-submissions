class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        d = {}
        start = 0
        maxResult = 0

        for end in range(len(s)):

            if s[end] not in d:
                d[s[end]] = 1
            else:
                d[s[end]] += 1

            while (end - start + 1) - max(d.values()) > k:
                d[s[start]] -= 1
                start += 1

            maxResult = max(maxResult, end - start + 1)

        return maxResult

        
        
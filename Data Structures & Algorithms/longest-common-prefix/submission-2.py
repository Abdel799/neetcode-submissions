class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        word1 = strs[0]
        word2 = strs[-1]
        prefix = ""

        for i in range (len(word1)):
            
            if word1[i] == word2[i]:
                prefix += word1[i]
            else:
                return prefix
        
        return prefix



        
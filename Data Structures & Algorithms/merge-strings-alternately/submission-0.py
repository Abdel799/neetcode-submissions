class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        newStr = ""

        p1 = 0
        p2 = 0

        while p1 < len(word1) or p2 < len(word2):

            if p1 < len(word1):
                
                newStr += word1[p1]
            
            if p2 < len(word2):

                newStr += word2[p2]
            
            p1 += 1
            p2 += 1
        
        return newStr
            
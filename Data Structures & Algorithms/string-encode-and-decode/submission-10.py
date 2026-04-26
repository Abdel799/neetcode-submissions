class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        if strs == []:
            s = "x"
            return s

        for i in range (0, len(strs)):
            if i != len(strs) - 1:
                
                if strs[i] == "":
                    s += ">?"

                else:
                    s += strs[i] + "?"
            
            else:
                s += strs[i]
        
        return s

    def decode(self, s: str) -> List[str]:
        arr = []
        temp = ""

        if s == "x":
            return arr
        
        for i in range (0, len(s)):
            if s[i] != "?":
                if s[i] == ">":
                    arr.append("")
                else:
                    temp += s[i]
            
            else:
                if temp != "":
                    arr.append(temp)
                    temp = ""
        
        arr.append(temp)
        
        return arr


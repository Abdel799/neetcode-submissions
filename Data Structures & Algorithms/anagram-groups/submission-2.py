class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            if "".join(sorted(s)) not in d:
                d["".join(sorted(s))] = [s]
            else:
                d["".join(sorted(s))].append(s)
        
        return list(d.values())
        
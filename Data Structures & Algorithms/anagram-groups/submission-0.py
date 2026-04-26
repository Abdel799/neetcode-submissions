class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        result = list()

        for item in strs:
            temp = ''.join(sorted(item))

            if temp not in myMap:
                myMap[temp] = list()
            
            myMap.get(temp).append(item)
        
        for key in myMap:
            result.append(myMap.get(key))
        
        return result
        
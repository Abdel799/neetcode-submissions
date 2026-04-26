class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []

        for i in range (len(temperatures)):
            count = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    count += 1
                
                else:
                    result.append(count)
                    count = 0
                    break
            
            if count != 0:
                result.append(0)
             
    
        return result
        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            
        result = [0] * len(temperatures)
        stack = []

        for i in range (len(temperatures)):
            if stack == [] or temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            
            else:
                
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        
        return result
                




        

        
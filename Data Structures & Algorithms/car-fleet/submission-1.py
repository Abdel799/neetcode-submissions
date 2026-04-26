class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        m = {}

        for i in range (len(position)):
            m[position[i]] = speed[i]
        
        position.sort(reverse=True)

        s = []

        for i in range (len(position)):

            time = (target - position[i]) / m[position[i]]

            if s:
                if s[-1] < time:
                    s.append(time)
            
            else:
                s.append(time)
        
        return len(s)

        
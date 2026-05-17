class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        d = {}

        for i in range (len(position)):
            d[position[i]] = speed[i]

        clone = sorted(position)
        clone.reverse()

        baseTime = (target - clone[0]) / d[clone[0]]
        st = [baseTime]

        for i in range (1, len(clone)):
            time = (target - clone[i]) / d[clone[i]]

            if time <= st[-1]:
                continue
            
            else:
                st.append(time)
        
        return len(st)

        
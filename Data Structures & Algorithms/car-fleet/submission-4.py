class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # hour = (target - miles) / mile/hour

        clone = sorted(position)
        clone.reverse()
        t = position.index(clone[0])

        baseTime = (target - clone[0]) / speed[t]
        st = [baseTime]

        for i in range (1, len(clone)):
            t = position.index(clone[i])
            time = (target - clone[i]) / speed[t]

            if time <= st[-1]:
                continue
            
            else:
                st.append(time)
        
        return len(st)

        
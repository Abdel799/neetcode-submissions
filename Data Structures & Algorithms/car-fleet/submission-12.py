class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # time it takes = (target - position) / speed

        times = [0] * len(position)
    
        d = {}

        for i in range (len(position)):
            d[position[i]] = speed[i]

        clone = position
        clone.sort()
        clone.reverse()

        for i in range (len(clone)):
            time = (target - clone[i]) / d[clone[i]]
            times[i] = time

        stack = []

        for time in times:
            if stack == [] or stack[-1] < time:
                stack.append(time)
            
            else:
                continue

        return len(stack)


        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        result = []

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        for i in range (k):
            m = max(d, key=d.get)
            result.append(m)
            d.pop(m)
        
        return result


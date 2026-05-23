class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0, 1, 1, 2, 3, 4, 5, 6]

        if nums == []:
            return 0

        new = sorted(nums)
        s = [new[0]]
        maxSeq = 1

        for i in range (1,len(new)):

            if new[i] == s[-1] + 1:
                s.append(new[i])
            elif new[i] == s[-1]:
                continue
            else:
                maxSeq = max(len(s), maxSeq)
                s = [new[i]]
        
        maxSeq = max(len(s), maxSeq)
        return maxSeq


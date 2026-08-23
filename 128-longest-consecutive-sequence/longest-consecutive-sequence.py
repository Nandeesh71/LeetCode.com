class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        HashSet = set(nums)
        longSeq = 0

        for num in HashSet:

            if num - 1 not in HashSet:
                next_num = num + 1
                SeqLength = 1

                while next_num in HashSet:
                    SeqLength += 1
                    next_num += 1

                longSeq = max(longSeq, SeqLength)
        
        return longSeq
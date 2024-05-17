class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 
        for n in nums:
            length = 0
            # This step is to find the start of a sequence 
            if n-1 not in numSet:
                while n+length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

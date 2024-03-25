class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Time Complexity: 

        nums.sort()
        res = 0 
        mod = (10**9 + 7)

        r = len(nums) - 1 
        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1 
            # means we found some values which can be added 
            if i <= r:
                # (r - i) -> means how many subsequences or choices we have 
                res += (2 ** (r - i))
                res %= mod 

        return res 

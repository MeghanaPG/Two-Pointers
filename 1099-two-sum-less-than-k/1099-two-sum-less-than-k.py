class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1 
        res = -1 

        while l < r:
            twoSum = nums[l] + nums[r]

            if twoSum < k:
                res = max(res, twoSum)
                l += 1 
            else:
                r -= 1
        
        return res
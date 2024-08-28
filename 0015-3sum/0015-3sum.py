class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curSum = a + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # However, if nums[l] == nums[l - 1], then using nums[l] in the next triplet would produce the same triplet as before.
                    while l <= r and nums[l] == nums[l - 1]:
                        l += 1
        return res

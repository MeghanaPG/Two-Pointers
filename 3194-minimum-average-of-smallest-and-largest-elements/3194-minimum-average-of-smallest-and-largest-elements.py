class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)//2):
            tmp = (nums[i] + nums[len(nums)-i-1])/2
            res = min(tmp,res)
        return res 
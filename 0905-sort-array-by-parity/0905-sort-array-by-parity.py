class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        # QuickSort
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] % 2 == 0: l += 1
            if nums[r] % 2 == 1: r -= 1

        return nums
            

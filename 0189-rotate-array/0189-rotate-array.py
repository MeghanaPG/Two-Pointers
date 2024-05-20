class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time Complexity: O(n)
        # The below solution can potentially lead upto O(n^2) if the 
        # the k vlaue is almost equal to n 
        # Two Pointers
        # i = 0 
        # r = len(nums) - 1 
        # while k!= 0:
        #     nums.insert(i, nums[r])
        #     nums.pop()
        #     r = len(nums) - 1 
        #     k -= 1 
        # return nums 

        # Time Compelxity: O(n)
        # Space Complexity: O(1)
        k = k % len(nums)
        l , r = 0, len(nums) - 1 
        while l < r:
            # first we reverse the entire array
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l+1, r-1 

        l , r = 0, k - 1
        # reverse the first k elements 
        while l < r:
            # first we reverse the entire array
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l+1, r-1 
        
        l , r = k, len(nums) - 1
        # reverse the remaining portions of the elements 
        while l < r:
        # first we reverse the entire array
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l+1, r-1 
        
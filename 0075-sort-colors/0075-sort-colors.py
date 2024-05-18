class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using bubble sort 
        # Bubble sort compares adjacent elements and sorts the array in place 
        # Time complexity: O(n^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(0, n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        # return nums 
        
        # Merge Sort 
        # Time complexity: O(nlogn)
        def merge_sort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2 
                L = nums[:mid]
                R = nums[mid:]
                merge_sort(L)
                merge_sort(R)
                i = j = k = 0 
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        nums[k] = L[i]
                        i += 1 
                    else:
                        nums[k] = R[j]
                        j += 1 
                    k += 1 
                #when we are left with only one array 
                while i < len(L):
                    nums[k] = L[i]
                    i += 1 
                    k += 1 
                while j < len(R):
                    nums[k] = R[j]
                    j += 1 
                    k += 1 
        merge_sort(nums)
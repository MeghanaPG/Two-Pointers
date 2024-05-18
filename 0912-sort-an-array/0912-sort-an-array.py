class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(nlogn)
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            # i is for array and j&k for the left and right half
            i, j, k = L, 0, 0 
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1 
                else:
                    arr[i] = right[k]
                    k += 1 
                # irrespective of the values we add we have to increase the i value 
                i += 1 
            while j < len(left):
                nums[i] = left[j]
                i += 1 
                j += 1 
            while k < len(right):
                nums[i] = right[k]
                i += 1 
                k += 1 

        def mergeSort(arr, l, r):
            if l == r:
                return arr 

            m = (l+r) // 2 
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            # merge part
            merge(arr, l, m, r)
            return arr 

        return mergeSort(nums, 0, len(nums)-1)
            
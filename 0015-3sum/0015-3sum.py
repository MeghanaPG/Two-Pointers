class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # Sorting: O(nlogn) + Two sum O(n^2)
    # Overall time complexity is O(n^2)
        res = []
        nums.sort()

        #To Handle the duplicate
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue 

            # two sum
            l,r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1 
                elif threeSum < 0:
                    l += 1 
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r: 
                        l += 1
        return res 
        
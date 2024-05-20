class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Time complexity will be O(n)
        #we are gonna start with index 1 
        left = 1
        
        #we are going to point both left and right pointers to 1st index 
        for right in range(1,len(nums)):
            if nums[right]!= nums[right-1]:
                #we will keep our new unique value in the left index 
                nums[left] = nums[right]
                left += 1
            #right += 1 here we need not increment the right pointer because our for loop is gonna handle that
        return left
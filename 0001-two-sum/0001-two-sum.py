class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i,j]
        
        num_dict = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement

            # Check if the complement exists in the dictionary
            if complement in num_dict:
                return [num_dict[complement], i]

            # If not found, add the current number and its index to the dictionary
            num_dict[num] = i
    
        return None  # If no solution is found
     
        
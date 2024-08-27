class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Time Complexity:
        neg_arr = []
        pos_arr = []
        res = []

        for n in nums:
            if n < 0:
                neg_arr.append(n)
            else:
                pos_arr.append(n)
        
        i = 0
        while i < len(pos_arr) and i < len(neg_arr):
            res.append(pos_arr[i])
            res.append(neg_arr[i])
            i += 1
            
        while i < len(pos_arr):
            res.append(pos_arr[i])
            i += 1

        # If there are any remaining elements in neg_arr
        while i < len(neg_arr):
            res.append(neg_arr[i])
            i += 1

        return res 

            
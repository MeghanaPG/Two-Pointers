class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # initial_max = -1
        # reverse iteration 
        # new_max = max(oldmax, arr[i])
        # we are computing in a way that you just have to look at the immediate next element 

        rightMax = -1

        for i in range(len(arr)-1, -1, -1):
            new_max = max(rightMax, arr[i])
            arr[i] = rightMax 
            rightMax = new_max 
        return arr



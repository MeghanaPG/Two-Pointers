class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time Complexity: O(n)
        l = 0
        r = len(s) - 1
        while l < r:
            helper_var = s[l]
            s[l] = s[r]
            s[r] = helper_var 
            l += 1 
            r -= 1 
        return s 


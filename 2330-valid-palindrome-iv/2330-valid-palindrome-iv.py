class Solution:
    def makePalindrome(self, s: str) -> bool:
        # Time Complexity: O(n)
        l = 0 
        r = len(s)-1

        count = 0 

        while l < r:
            if s[l] != s[r]:
                count += 1
                if count > 2:
                    return False
            l += 1
            r -= 1
        return True 

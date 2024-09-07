class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare the characters at the pointers
            if s[left].lower() != s[right].lower():
                return False
            
            # Move the pointers closer to the center
            left += 1
            right -= 1
        
        return True

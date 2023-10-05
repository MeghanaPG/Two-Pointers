class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_S = ""
        for char in s:
            if char.isalnum():
                new_S += char
                new_S = new_S.lower()
        if new_S == new_S[::-1]:
            return True 
        else: 
            return False 
        
        
        
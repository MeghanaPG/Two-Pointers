class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0  # pointer for str2

        for i in range(len(str1)):
            # Check if the current character matches str2[j] or its cyclic increment
            if j < len(str2) and (str1[i] == str2[j] or ('a' if str1[i] == 'z' else chr(ord(str1[i]) + 1)) == str2[j]):
                j += 1  # move to the next character in str2
            
            # If we've matched all characters in str2, return True
            if j == len(str2):
                return True

        # If we finish looping through str1 and haven't matched all of str2
        return j == len(str2)


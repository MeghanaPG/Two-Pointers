class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Time Complexity: O(n)
        w1_l, w1_r = 0, len(word1) - 1 
        w2_l, w2_r = 0, len(word2) - 1 
        res = ""

        while w1_l <= w1_r and w2_l <= w2_r:
            res += word1[w1_l]
            res += word2[w2_l]
            w1_l += 1 
            w2_l += 1 
        
        if len(word1) > len(word2):
            res += str(word1[len(word2):])

        if len(word2) > len(word1):
            res += str(word2[len(word1):])
        
        return res 
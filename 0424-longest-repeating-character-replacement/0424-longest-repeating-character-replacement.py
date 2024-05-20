class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Sliding Window Technique
        #Time complexity: O(26n)
        #condition: windowlen - count[B] >= k 
        #We will expand the window as long as the condition is valid 
        count = {}
        res = 0 
        
        l = 0 
        maxf = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            #condition
            while(r -l + 1) - maxf > k:
                #now we want to increment the left pointer and also we will have to 
                #decrement the count of the left pointer
                count[s[l]] -= 1 
                l += 1 
                
            res = max(res, r-l+1)
        return res 
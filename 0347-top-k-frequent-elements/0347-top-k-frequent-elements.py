from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #Time complexity:O(n)
    #Bucket Sort 
    #We will have the count and values (count will be 0,1,2,...) and values
    #will correspond to how many values are occuring that many times.
    #Then we will return based on the reverse order, high number of occurences 
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            #count is the key and n is the value 
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
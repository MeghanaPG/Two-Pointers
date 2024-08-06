class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Two Pointers 
        # Time Complexyity: O(n)
        n = len(prices)
        start = 0 
        total_periods = 0

        for end in range(n):
            if end > 0 and prices[end] != prices[end-1] - 1:
                start = end 
            
            total_periods += end - start + 1 
        return total_periods 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Time complexity: O(n)
        #monotonically decreasing queue
        output = []
        q = collections.deque() #index
        l = r = 0 
        
        while r < len(nums):
            #while q is non empty and right most value of the queue is less than the 
            # value we are inserting then we can pop and append value at nums[r]
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # to handle the window
            # remove left value from window 
            if l > q[0]:
                q.popleft()
            
            #making sure that the window is size k to update the window 
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1 
            r += 1 
            
        return output 
            
       




class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0 

        left, right = 0, len(height) - 1
        while left < right:
            rec_length = min(height[left], height[right])
            rec_breadth = right - left
            area = rec_length * rec_breadth 
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1 
        return maxArea 
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) -1 

        while start < end:
            current_sum = numbers[start] + numbers[end]

            if current_sum == target:
                return [start+1, end+1]
            elif target > current_sum:
                start += 1
            else:
                end -= 1
                
        return None 
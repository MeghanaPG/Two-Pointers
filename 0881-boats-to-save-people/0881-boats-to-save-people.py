class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
    # Time Complexity: O(nlogn)
    # Two Pointers
        people.sort()
        l, r = 0, len(people) - 1
        no_of_boats = 0

        while l <= r:
             remain = limit - people[r]
             r -= 1
             no_of_boats += 1 
            # can we take the lightest person now and also put them on the boat
             if l <= r and remain >= people[l]:
                l += 1
        return no_of_boats
            

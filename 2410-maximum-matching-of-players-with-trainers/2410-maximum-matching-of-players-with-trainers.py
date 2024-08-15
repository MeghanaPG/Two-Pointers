class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Time Complexity: O(nlogn)
        # Two Pointers
        trainers.sort()
        players.sort()

        res = 0
        i, j = 0, 0 

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res += 1 
                i += 1
            j += 1 
        
        return res 



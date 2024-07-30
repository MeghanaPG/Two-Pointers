class Solution:
    def pivotInteger(self, n: int) -> int:
        # 2 pointer solution 
        p, q = 0, n 
        sump, sumq = 0, 0

        while p <= q:
            if sump < sumq:
                sump += p
                p += 1 
            else:
                sumq += q
                q -= 1 
            
        return p if sump + p == sumq else -1 
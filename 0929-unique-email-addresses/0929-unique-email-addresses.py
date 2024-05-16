class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Time complexity:O(n+m)
        unique = set()

        for e in emails:
           i, local = 0, ""
           #local
           while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                # even if we encounter we just proceed 
                i += 1 
            #domain
           while e[i]!= "@":
                i += 1 
           domain = e[i+1:]
           unique.add((local,domain))
        return len(unique)
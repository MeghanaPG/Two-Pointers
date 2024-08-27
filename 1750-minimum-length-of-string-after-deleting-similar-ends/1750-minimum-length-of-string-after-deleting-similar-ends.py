class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            tmp = s[l]
            # These loops "shrink" the string by removing consecutive matching characters from both ends until the characters at l and r differ or the pointers cross.
            while l <= r and s[l] == tmp:
                l += 1
            while l <= r and s[r] == tmp:
                r -= 1
        return (r-l+1)

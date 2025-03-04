class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p_1 = p_2 = 0
        while p_1 < len(s) and p_2 < len(t):
            if s[p_1] == t[p_2]:
                p_1 += 1
            p_2 += 1
        return p_1 >= len(s)
 

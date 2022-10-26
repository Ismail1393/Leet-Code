class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        leftBound,rightBound = len(s), len(t)
        
        p_s =p_t = 0
        
        while p_s < leftBound and p_t < rightBound:
            
            if s[p_s] == t[p_t]:
                p_s += 1 
            p_t += 1
        
        return p_s == leftBound
        
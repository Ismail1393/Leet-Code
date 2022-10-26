class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping1= {}
        mapping2 = {}
        
        for c1,c2 in zip(s,t):
            
            if (c1 not in mapping1) and (c2 not in mapping2):
                mapping1[c1] = c2
                mapping2[c2]= c1
                
            elif mapping1.get(c1) != c2 or mapping2.get(c2) != c1:
                return False 
            
        return True
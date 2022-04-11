class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns = len(s) #2
        nt = len(t) #3
        
        if ns > nt : # False
            return self.isOneEditDistance(t,s)
        
        if nt - ns >1: # false
            return False
        
        for i in range(ns): # 0,2
            if s[i] != t[i]: 
           
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
                
        return ns +1 == nt
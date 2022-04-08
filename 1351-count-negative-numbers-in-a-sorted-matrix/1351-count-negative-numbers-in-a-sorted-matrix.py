class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        ans=[]
        
        for i in grid:
            ans+=i
        
        return sum([i<0 for i in ans])
            
        
        
        
        

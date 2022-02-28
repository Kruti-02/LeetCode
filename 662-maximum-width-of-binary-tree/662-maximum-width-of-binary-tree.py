# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [(root,0)]
        width = 1
        
        while queue:
            if len(queue)>1:
                width = max(width,queue[-1][1] - queue[0][1] +1)
            next_queue =[]
            while queue:
                node,position = queue.pop(0)
                if node.left:
                    next_queue.append((node.left,position*2))
                if node.right:
                    next_queue.append((node.right,position*2 +1))
            queue = next_queue
                
        return width
                    
                    
            
            
        
        
        
        
        
   
    
        
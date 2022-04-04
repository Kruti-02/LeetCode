class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        left = 0
        right = len(s)-1
        
        for i in range(len(s)):
            while left < right:
                s[left],s[right] = s[right],s[left]
                left,right = left+1, right-1
        """
        Do not return anything, modify s in-place instead.
        """
        
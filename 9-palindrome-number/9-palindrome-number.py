class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        multiplier =1
        while x >= 10 * multiplier:
            multiplier *=10
            
        while x>0:
            if x // multiplier != x % 10:
                return False
            
            x = (x % multiplier)//10
            multiplier = multiplier / 100
        return True
            
        
        
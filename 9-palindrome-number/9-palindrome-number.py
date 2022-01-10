class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        #negative = False
        if x < 0 :
            return False
        while x>0:
            digit = x % 10
            rev = rev*10 + digit
            x = x // 10
        if temp == rev:
            return True
        #if negative:
            #return False
     
        
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numstack=[]
        
        for digit in num:
            while k and numstack and numstack[-1] > digit:
                numstack.pop()
                k -= 1
                
            numstack.append(digit)
                
        finalstack = numstack[:-k] if k else numstack
        
        return "".join(finalstack).lstrip('0') or "0"
                
        
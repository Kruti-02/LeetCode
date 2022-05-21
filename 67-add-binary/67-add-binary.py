class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #conver binnary to int
        a,b = int(a,2), int(b,2)
        #add the number
        res = a + b
        #return the binnary
        return '{0:b}'.format(res)
  
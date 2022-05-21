class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary numbers to integer
        a,b = int(a,2), int(b,2)
        #print(a,b)
        # Add
        result = a+b
        # Convert integer to binary string
        return '{0:b}'.format(result)        
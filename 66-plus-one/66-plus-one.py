class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert array of digits into a string
        num = ""
        for element in digits:
            num += str(element)
        
        # Convert that string into integer
        num = int(num)
        
        # Add 1 to the integer
        num +=1
        
        # Convert the integer to an array
        res = [int(x) for x in str(num)]
        
        # Return
        return res
        
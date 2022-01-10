class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        i = 0
        while i< len(s):
            initial_val = self.get_int_value(s[i])
            if i+1 < len(s):
                next_val = self.get_int_value(s[i+1])
            else:
                next_val = 0
            if next_val > initial_val:
                output = output + (next_val - initial_val)
                i+=1
            else:
                output = output + initial_val
            i+=1
        return output
            
                
    def get_int_value(self,c):
        dict = {"I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000}
        return dict[c]
        
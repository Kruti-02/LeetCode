class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = ""
        answer=[]
        for i in range(0,n):
            index = i+1
            if index%3 == 0:
                result+= "Fizz"
                if index%5 == 0:
                    result+= "Buzz"
            elif index%5 ==0:
                result+= "Buzz"
            else:
                result = str(index)
            answer.append(result)
            result =""
        return answer
                
                    
        
        
                
            
            
        
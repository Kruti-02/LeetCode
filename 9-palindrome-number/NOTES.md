obtain the last digit of the number , by `%10` operation.
​
compare it with the first digit of the number   (obtaining the first digit )
multiplier = 1, while num >=10*multiplier : ; multiplier *= 10.
​
if first and last digit match the number may be pallindrome else return false.
​
if first and last digit match, remove those two digit with formulla:
```  x = ( x % div ) // 10  ```  and then change ```multiplier = multiplier/100``` (as two digits are removed from the numbers.)
​
​
​
​
number = 0
multiplier = 10 ** (len(digits) - 1)
for digit in digits:
number = number + digit * multiplier
multiplier = multiplier//10
#print(number)
number +=1 # 4322
result = []
while number:
result.insert(0, number%10) #[]
number = number//10
return result
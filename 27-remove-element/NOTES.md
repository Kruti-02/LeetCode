Use left pointer as traversal pointer
Use right pointer as dump pointer
​
IF `nums[left] == val` then put it at dump location and decrement dump pointer
​
else check next element
​
return the position of `dump pointer + 1` because that indicates remaining elements.
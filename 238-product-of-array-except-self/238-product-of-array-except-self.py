class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Create a result output array Innitially with 1 and multiply it by lem nums
        res = [1]*len(nums)
        #Calculate the prefix by innitializing it by 1
        prefix = 1
        #Go to every position in our input array
        for i in range(len(nums)):
            #for each number in res i thake it and put it in prefix
            res[i] = prefix
            #Multiply the nums i by the prefix value
            prefix *= nums[i]
        #Innitiate the postfix array
        postfix = 1
        #Iterate through the inputs from behind  until the begining
        for i in range(len(nums)-1,-1,-1):
            #multiply the result i with the postfix values
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
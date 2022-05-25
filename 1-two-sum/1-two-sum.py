class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create a hash_map where key = element of nums and value is the index of that element
        hash_map = {}
        #Iterating through every value in array
        for i,n in enumerate(nums):
            #Check the difference
            diff = target - n
            #Check if difference exist in hashmap
            if diff in hash_map:
                return [hash_map[diff],i]
            #If element does't exixst to map add that element
            hash_map[n] = i
        return
        
        
            
        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset
        hash_set = set()
        #Go to every value in array  
        for n in nums:
            #check if number already exist in hash_set
            if n in hash_set:
                return True
            #add each value to the hash_set
            hash_set.add(n)
        return False
        
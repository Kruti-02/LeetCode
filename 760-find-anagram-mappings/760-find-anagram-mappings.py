class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
       
        
        for number in nums1:
            output.append(nums2.index(number))
        
        return output
        
        
        
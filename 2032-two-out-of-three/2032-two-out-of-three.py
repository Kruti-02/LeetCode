class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        output = []
        frequencies = {}
        
        for nums_array in [nums1, nums2, nums3]:
            for num in list(set(nums_array)):
                if num in frequencies:
                    frequencies[num] +=1
                else:
                    frequencies[num] = 1
        
        for num in frequencies:
            if frequencies[num] > 1:
                output.append(num)
        
        return output
                
        
        
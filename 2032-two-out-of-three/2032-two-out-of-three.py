class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        output = []
        
        set_n1 = set(nums1)
        set_n2 = set(nums2)
        set_n3 = set(nums3)
        
        return list((set_n1 & set_n2).union((set_n2 & set_n3)).union((set_n3 & set_n1)))
        
        
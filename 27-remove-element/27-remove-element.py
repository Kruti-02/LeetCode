class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        k=len(nums)
        j=len(nums)-1
        
        while (i<len(nums)):
            if nums[i] == val:
                nums[i] = nums[j]
                nums[j] = '_'
                k-=1
                j -= 1
                
            else:
                i +=1
        
        return k
    
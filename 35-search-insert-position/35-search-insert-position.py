class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1] :
            return len(nums)
        if target < nums[0]:
            return 0
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
            elif nums[i+1] > target:
                return i+1
        return 0
            
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        print (nums)
        mid = len(nums)//2
        #print(mid)
        return nums[mid]
        
                
        
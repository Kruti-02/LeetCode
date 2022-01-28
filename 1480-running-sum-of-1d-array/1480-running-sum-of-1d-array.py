class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        runningsum=0
        for numbers in nums:
            runningsum += numbers
            ans.append(runningsum)
        return ans
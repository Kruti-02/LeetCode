class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0
        running_sum = []
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        return running_sum

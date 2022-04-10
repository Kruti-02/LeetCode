class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n  < 3:
            return 0
        
        two_sums = defaultdict(int)
        two_sums[nums[0]+nums[1]] += 1
        
        ans=0
        
        
        for i in range(2,n):
            for two_sum in two_sums:
                if two_sum + nums[i] < target:
                    ans += two_sums[two_sum]
                    
            for j in range(i):
                two_sums[nums[i] + nums[j]] += 1
                
        return ans
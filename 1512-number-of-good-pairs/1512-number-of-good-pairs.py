class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        cnt = 0
        for v in nums:
            if v in d.keys():
                cnt+=d[v]
                d[v]+= 1
            else:
                d[v]=1
        return cnt
        
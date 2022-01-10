class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0,len(nums)):
            map[nums[i]] = i
        
        #print(map)
        
        for i in range(0, len(nums)):
            key = target - nums[i]
            #print(map)
            if key in map.keys():
                if map.get(key) != i:
                    #print(map)
                    return [i, map.get(key)]
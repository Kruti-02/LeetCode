class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        counter = {}
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
        results = []
        for key, value in counter.items():
            if value == 1:
                results.append(key)
        print(results)
        
        if not results:
            return -1
        
        results = sorted(results)
        
        return results[-1]
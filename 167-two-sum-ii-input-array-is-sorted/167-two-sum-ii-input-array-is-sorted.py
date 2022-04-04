class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        keymap = {}
        
        for i,n in enumerate(numbers):
            diff = target-n
            if diff in keymap:
                return [keymap[diff],i+1]
            keymap[n] = i+1
        return
            
        
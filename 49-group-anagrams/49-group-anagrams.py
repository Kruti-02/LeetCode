class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a hashmap having key as a character_count of words and values as list of anagrams
        res = defaultdict(list)
        #Go through every string of the input
        for s in strs:
            count = [0]*26
        #Map a to index0 and z to index 25 by subtracting the current asci_val of character with asci_val of a
            for c in s:
                count[ord(c) - ord("a")] += 1
            
        #Append string to the result
            res[tuple(count)].append(s)
        return res.values()
        
        
        
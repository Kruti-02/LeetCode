class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle = ['']*len(s)
        for index,character in enumerate(indices):
            shuffle[character] = s[index]
        return "".join(shuffle)
            
            
            
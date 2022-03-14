class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        w1 = ""
        w2 = ""
        for word in word1:
            w1+=str(word)
        for wor in word2:
            w2+=str(wor)
            
        if w1 == w2:
             return True
        else:
            return False
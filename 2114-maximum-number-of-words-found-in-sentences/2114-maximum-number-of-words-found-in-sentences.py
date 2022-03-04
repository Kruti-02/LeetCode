class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lst=[]
            
        for i in range(len(sentences)):
            word=sentences[i]
            count=len(word.split(' '))
            lst.append(count)
        return(max(lst))
        
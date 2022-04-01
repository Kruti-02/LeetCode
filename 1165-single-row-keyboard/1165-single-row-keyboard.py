class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        layout = {}
        time = 0
        index = 0
        for i in range(len(keyboard)):
            layout[keyboard[i]] = i
        
        for c in word:
            time += abs(index - layout[c])
            index = layout[c]
        return time
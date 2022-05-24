class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if length of s and t are equal
        if len(s) != len(t):
            return False
        #Count the character in both the strings
        countS, countT = {}, {}
        #go through the strings at the same time
        for i in range(len(s)):
            #Count the character of the string it is key in the hashmap
            #if the character doesnt exist python will throw error for that use get fnction
            countS[s[i]] = 1+ countS.get(s[i], 0)
            countT[t[i]] = 1+ countT.get(t[i], 0)
        #For iterating through the hashmap and make sure counts are the same
        for c in countS:
            if countS[c] != countT.get(c, 0):
                    return False
        return True
        
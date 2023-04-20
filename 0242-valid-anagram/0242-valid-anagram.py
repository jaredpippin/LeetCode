class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #build the HashMap
        sCounts, tCounts = {}, {}
        for i in range(len(s)):
            sCounts[s[i]] = sCounts.get(s[i],0) + 1
            tCounts[t[i]] = tCounts.get(t[i],0) + 1
            
        for j in sCounts:
            if sCounts[j] != tCounts.get(j,0):
                return False
        return True
        
        
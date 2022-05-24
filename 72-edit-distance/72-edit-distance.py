class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        ED = [[0 for x in range(n+1)] for x in range(m+1)]
        for i in range(m+1):  
            for j in range(n+1):
                if (i == 0):
                    ED[i][j] = j
                elif (j == 0):
                    ED[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    ED[i][j] = ED[i-1][j-1]
                else:
                    ED[i][j] = 1 + min(ED[i-1][j],ED[i][j-1], ED[i-1][j-1])
    
        return ED[m][n]
    
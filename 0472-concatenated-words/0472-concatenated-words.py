class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dp(s):
            n = len(s)
            
            dp = [False] * (n+1)
            dp[0] = True
            
            for i in range(1, n+1):
                for j in range(i):
                    if dp[j] and s[j:i] in wordSet and s[j:i] != s:
                        dp[i] = True
                        break
            return dp[n]
        
        ans = []
        
        wordSet = set(words)
        
        for word in words:
            if dp(word):
                ans.append(word)
                
        return ans
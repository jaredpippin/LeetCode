class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        combos = [0] * (amount + 1)
        for j in range(1,amount+1):
            minimum = 1000000
            for i in range(1,len(coins)+1):
                if (j >= coins[i-1]):
                    minimum = min(minimum, 1+combos[j-coins[i-1]])
                combos[j] = minimum
        
        if (combos[amount] == 1000000):
            combos[amount] = -1
        return combos[amount]
        
        
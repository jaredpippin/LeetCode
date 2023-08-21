class Solution:
    def climbStairs(self, n: int) -> int:
        #solution always just depends on the two entries before it, working backwards
        
        one, two = 1,1 #setting two variables for storing our number of options, will be sliding throughout
        
        #always checking n-1 times
        #we know that at the final and final-1 steps, it takes 1 and 2 step respectively
        for i in range(n-1):
            temp = one #store one's amount
            one = one + two #one will become the combo of the two entries before it (moved to slot to left)
            two = temp #set back to one's amount
            
        return one #one will eventually be at the leftmost slot, contains our solution as we are at the beginning
            
            
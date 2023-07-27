# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #use binary search
        
        low,high = 1,n
        badBegin = n
        
        while (low <= high):
            mid = (low + high) // 2
            
            #if the midpoint is bad, then the start can be to the left
            if (isBadVersion(mid)):
                badBegin = mid #current known earliest bad version
                high = mid-1 #move to the left
            else:
                low = mid+1 #move to the right if the current isn't bad
        return badBegin
        
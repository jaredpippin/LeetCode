class Solution:
    def tribonacci(self, n: int) -> int:
        t0,t1,t2 = 0,1, 1 #to keep track
        if n == 0: #base case t0
            return t0
        if n == 1 or n == 2: #base case t1/t2
            return t1
        for i in range(3, n+1): #t(n+3) = t(n) + t(n+1) + t(n+2) which means, t(n) = t(n-3) + t(n-2) + t(n-1)
            #t_n will equal the previous 3 entries
            tn = t0 + t1 + t2  #t(3) = t(0) + t(1) + t(2), #t(4) = t(1) + t(2) + t(3)
            #count everything up
            t0 = t1 #t(0) -> t(1), #t(1) -> t(2)
            t1 = t2 #t(1) -> t(2), #t(2) -> t(3)
            t2 = tn #t(2) -> t(3), #t(3) -> t(4)
        return tn
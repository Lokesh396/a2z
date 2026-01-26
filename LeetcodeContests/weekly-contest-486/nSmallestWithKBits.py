# Wrote brute force solution not submitted as optimal solution was not known

class Solution:
    def setbitCount(self,n):
        cnt = 0
        while n:
            cnt += 1
            n = n & (n-1)
        return cnt
            
    def nthSmallest(self, n: int, k: int) -> int:
        cnt = 0
        i = (1 <<k) -1
        while True:
            if self.setbitCount(i) == k:
                cnt += 1
            if cnt == n:
                return i
            i += 1
class Solution:
    hm = {}
    def fib(self, n: int) -> int:
        
        if n ==1 :
            return 1
        if n == 0:
            return 0

        if n in self.hm:
            return self.hm[n]

        self.hm[n] =  self.fib(n-1) + self.fib(n-2)          

        return self.hm[n]   
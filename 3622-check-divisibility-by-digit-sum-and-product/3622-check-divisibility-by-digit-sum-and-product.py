class Solution:
    def checkDivisibility(self, n: int) -> bool:
        og = n
        total = 0
        product = 1
        while n:
            digit = n % 10 
            total += digit
            product *= digit

            n = n//10

        return og % (total +product) ==0


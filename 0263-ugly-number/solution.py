class Solution:
    def isUgly(self, n: int) -> bool:
        primeFactors = [2, 3, 5]

        for num in primeFactors:
            while n > 1 and n % num == 0:
                n = n // num
        
        if n == 1:
            return True

        return False

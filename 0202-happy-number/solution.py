class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while n != 1:
            n = sum([int(v) ** 2 for v in str(n)])
            if n in d:
                return False
            else:
                d[n] = 0
        return True

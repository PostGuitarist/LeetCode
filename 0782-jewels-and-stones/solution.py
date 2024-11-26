class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        mySet = set(jewels)

        for stone in stones:
            if stone in mySet:
                count += 1

        return count

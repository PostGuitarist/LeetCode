class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        curr = 0

        for i in gain:
            curr += i
            maxAlt = max(maxAlt, curr)
        
        return maxAlt

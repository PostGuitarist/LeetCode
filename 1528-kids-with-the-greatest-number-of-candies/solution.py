class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        output = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                output.append(True)
            else:
                output.append(False)

        return output

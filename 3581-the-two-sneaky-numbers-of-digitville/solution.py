class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seenSet = set()
        newSet = []

        for num in nums:
            if num in seenSet:
                newSet.append(num)
            seenSet.add(num)

        return newSet

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniqueList = []

        for num in nums:
            if (num not in uniqueList) and (num > 0):
                uniqueList.append(num)

        return len(uniqueList)

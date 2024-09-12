class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seenSet = {}

        for n in range(len(nums)):
            if nums[n] in seenSet and abs(n - seenSet[nums[n]]) <= k:
                return True
            seenSet[nums[n]] = n

        return False

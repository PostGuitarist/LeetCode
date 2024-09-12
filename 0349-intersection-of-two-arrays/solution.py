class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = set()

        for num in nums1:
            if num in nums2:
                intersect.add(num)

        return list(intersect)

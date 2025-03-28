class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0

        for i in nums:
            if step < 0:
                return False
            elif i > step:
                step = i
            step -= 1

        return True 

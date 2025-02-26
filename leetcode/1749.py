class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        i = 0
        s = 0
        while i <= len(nums) - 1:
            s = 0
            a = nums[i]
            b = nums[i + 1]
            if abs(a + b) > s:
                s = abs(a + b)
            i += 1
        return s
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new = [0] * len(nums)
        j = 0
        for i in nums:
            new[j] = nums[i]
            new += 1
        return new

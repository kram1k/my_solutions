from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def _sum_array(array: int) -> int:
            res = 0
            for num in array:
                res += num
            return res
        l, r, mx = 0, k, -float("inf")
        if len(nums) <= k:
            return _sum_array(nums) / k
        while r <= len(nums):
            sum = _sum_array(nums[l:r])
            if mx < sum / k:
                mx = sum / k 
            l += 1
            r += 1
        return mx

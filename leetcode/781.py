from typing import List
from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        pairs = 0

        for num in nums:
            if d[k - num] > 0:
                pairs += 1
                d[k - num] -= 1
            else:
                d[num] += 1
        return pairs


sol = Solution()
print(sol.maxOperations(nums=[3,1,5,1,1,1,1,1,2,2,3,2,2], k=1))
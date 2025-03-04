class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            nums = nums
        else:
            c = 0
            i = 0
            while i < len(nums):
                if nums[i] == 0:
                    nums.remove(nums[i])
                    c += 1
                    if i != 0:
                        i -= 0
                else:
                    i += 1
            nums += [0 for _ in range(c)]


print(Solution.moveZeroes([0,1,0,3,12]))

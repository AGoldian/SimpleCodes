class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            digit = target - nums[i]
            slice_nums = (nums[:i] + [None] + nums[i+1:])

            if digit in slice_nums:
                return [i, slice_nums.index(digit)]



test_func = Solution().twoSum

assert test_func([3, 3], 6) == [0, 1]

print('Tests done, program work!')
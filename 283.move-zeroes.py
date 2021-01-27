#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Strategy 1: 2 pointers
        Runtime:O(n)
        space: O(1)

        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return

# @lc code=end

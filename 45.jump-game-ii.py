#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """ Strategey 1: Greedy
        Runtime: O(n), where n is the number of integers
        Space: O(1)

        Args:
            nums (List[int]): list of non-negative integers

        Returns:
            int: minimum of steps that can reach from index 0 to the end of
        """

        n = len(nums)
        if n < 2:
            return 0

        maxSteps = nums[0]
        maxPos = nums[0]
        jumps = 1

        for i in range(1, n):
            if maxSteps < i:
                jumps += 1
                maxSteps = maxPos
            maxPos = max(nums[i] + i, maxPos)
        return jumps

# @lc code=end

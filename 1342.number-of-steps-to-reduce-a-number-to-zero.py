#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
from abc import abstractmethod


class Solution:
    def numberOfSteps(self, num: int) -> int:
        """ Strategy 1: Linear scan
        Runtime:O(log(num))

        Args:
            num (int): a non-negative integer

        Returns:
            int: number of steps to reduce 0
        """

        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps
# @lc code=end

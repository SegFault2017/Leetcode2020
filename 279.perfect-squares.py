#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

from abc import ABCMeta, abstractmethod
import math

# @lc code=start


class Solution:
    def numSquares(self, n: int) -> int:
        """ Strategey 1: Dynamic Programming
        Runtime :O(n)
        Space:O(n)

        Args:
            n (int): a non negative integer

        Returns:
            int: the least number of perfect square numbers that sum to n
        """

        y = math.sqrt(n)
        if n % y == 0:
            return 1
        sqrt_nums = [i**2 for i in range(int(math.sqrt(n))+1)]
        dp = [n] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for sqr in sqrt_nums:
                if i < sqr:
                    break
                dp[i] = min(dp[i], dp[i-sqr] + 1)
        return dp[-1]


# @lc code=end

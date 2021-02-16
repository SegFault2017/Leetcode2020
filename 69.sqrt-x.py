#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
from math import e, log

# @lc code=start


class Solution:
    # def mySqrt(self, x: int) -> int:
    #     """ Startegey 1: Pocket Calculator
    #     Runtime: O(1)
    #     Space: O(1)

    #     Args:
    #         x (int): the number x

    #     Returns:
    #         int: sqaure root of x with truncated part
    #     """

    #     if x < 2:
    #         return x

    #     left = int(e ** (0.5 * log(x)))
    #     right = left + 1
    #     return left if right ** 2 > x else right

    def mySqrt(self, x: int) -> int:
        """ Startegey 1: Binary Search
        Runtime: O(log(x))
        Space: O(1)

        Args:
            x (int): the number x

        Returns:
            int: sqaure root of x with truncated part
        """
        if x < 2:
            return x
        low, high = 0, x//2

        while low <= high:
            mid = low + (high - low)//2
            num = mid**2
            if num > x:
                high = mid-1
            elif num < x:
                low = mid + 1
            else:
                return mid
        return high

    # * Newton method is has the least # of iteration when computing this problem


# @lc code=end

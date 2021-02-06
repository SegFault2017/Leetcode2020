#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    # def climbStairs(self, n: int) -> int:
    #     """ Strategey 1: Dynamic Programming
    #     Runtime: O(n)
    #     Space: O(n)

    #     Args:
    #         n (int): a non-negative integer

    #     Returns:
    #         int: number of ways to reach nth step
    #     """

    #     if n <= 2:
    #         return n

    #     dp = [0] * (n+1)

    #     for i in range(3, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]

    #     return dp[-1]

    def climbStairs(self, n: int) -> int:
        """ Strategey 1: Dynamic Programming 2
        Runtime: O(n)
        Space: O(1)

        Args:
            n (int): a non-negative integer

        Returns:
            int: number of ways to reach nth step
        """

        if n <= 3:
            return n

        x, y = 2, 3
        output = 0

        for _ in range(4, n+1):
            output = x + y
            x = y
            y = output
        return output

        # @lc code=end

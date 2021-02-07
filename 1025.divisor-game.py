#
# @lc app=leetcode id=1025 lang=python3
#
# [1025] Divisor Game
#

# @lc code=start
class Solution:
    def divisorGame(self, N: int) -> bool:
        """ Strtegey 1: Math
        Runtime: O(1)
        Space: O(1)

        Args:
            N (int): an positive integer

        Returns:
            bool: check whether alice win or not
        """

        return N % 2 == 0
# @lc code=end

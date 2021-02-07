#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """ Strategey 1: Dynamic Programming

        Args:
            cost (List[int]): cost of each step

        Returns:
            int: the minimum cost to reach from bottom to the top of the floor
        """

        f1 = f2 = 0

        for x in cost:
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
# @lc code=end

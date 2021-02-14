#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """ Strategey 1: Dynamic Programming
        Runtime: O(n *m), where n is the # of rows and m is the # of cols
        Space:O(1)

        Args:
            grid (List[List[int]]): each cell in the grid has a non-negative value

        Returns:
            int: return the minimum sum path
        """

        n = len(grid)
        m = len(grid[0])

        for i in range(1, n):
            grid[i][0] = grid[i-1][0] + grid[i][0]

        for i in range(1, m):
            grid[0][i] = grid[0][i-1] + grid[0][i]

        for y in range(1, n):
            for x in range(1, m):
                grid[y][x] = min(grid[y-1][x], grid[y][x-1]) + grid[y][x]
        return grid[-1][-1]

        # @lc code=end

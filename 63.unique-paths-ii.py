#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """ Strategey 1: Dynamic Programming
        Runtime: O(n*m)
        Space: O(n*m)

        Args:
            obstacleGrid (List[List[int]]): the grid with either obstacle(1) cell or empty(0) cell

        Returns:
            int: # of possible ways to go from top left to  reach bottom right
        """

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        OBSTACLE = 1
        EMPTY = 0

        if obstacleGrid[0][0] == OBSTACLE or obstacleGrid[-1][-1] == OBSTACLE:
            return 0

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            if obstacleGrid[i][0] == OBSTACLE:
                break
            dp[i][0] = 1

        for i in range(m):
            if obstacleGrid[0][i] == OBSTACLE:
                break
            dp[0][i] = 1

        for y in range(1, n):
            for x in range(1, m):
                if obstacleGrid[y][x] == OBSTACLE:
                    continue
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[-1][-1]


# @lc code=end

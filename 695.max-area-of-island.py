#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Strategy 1: BFS
        Runtime: O(n * m), where n is the # of rows and m is the # of columns
        Space: O(n * m)

        Args:
            grid (List[List[int]]): the grid

        Returns:
            int: maximum area of an island
        """

        if not grid:
            return

        n, m = len(grid), len(grid[0])
        WATER, LAND = 0, 1
        max_area = 0

        def valid(y: int, x: int) -> tuple:
            for r, c in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 <= r < n and 0 <= c < m and grid[r][c] == LAND:
                    yield (r, c)

            return ()

        def bfs(y: int, x: int) -> int:
            area = 1
            Q = [(y, x)]
            grid[y][x] = WATER

            while Q:
                y, x = Q.pop(0)
                for r, c in valid(y, x):
                    grid[r][c] = WATER
                    Q.append((r, c))
                    area += 1

            return area

        for y in range(n):
            for x in range(m):
                if grid[y][x] == LAND:
                    max_area = max(max_area, bfs(y, x))
        return max_area


# @lc code=end

#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from itertools import product


class Solution:
    from itertools import product

    def solve(self, board: List[List[str]]) -> None:
        """
        Strategy 1: DFS
        Do not return anything, modify board in-place instead.
        Runtime: O(n * m), where n is the # of rows in the board, and m is the # of cols in the board.
        Space: O(n* m)
        """

        WALL = "X"
        STONE = "O"
        ESCAPE = "E"
        if not board:
            return

        n, m = len(board), len(board[0])

        borders = list(product(range(n), [0, m-1])) + \
            list(product([0, n-1], range(m)))

        def valid(y: int, x: int) -> tuple:
            for r, c in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 <= r < n and 0 <= c < m:
                    yield (r, c)
            return ()

        def dfs(y: int, x: int) -> None:
            if board[y][x] == WALL:
                return
            board[y][x] = ESCAPE

            for r, c in valid(y, x):
                if board[r][c] == STONE:
                    dfs(r, c)
            return

        for y, x in borders:
            dfs(y, x)

        # print(board)

        for y in range(n):
            for x in range(m):
                if board[y][x] == STONE:
                    board[y][x] = WALL
                elif board[y][x] == ESCAPE:
                    board[y][x] = STONE
        return

# @lc code=end

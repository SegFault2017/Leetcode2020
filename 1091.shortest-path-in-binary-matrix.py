#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     """ Strategey 1: BFS
    #     Runtime: O(n^2), where n is the # of rows
    #     Space: O(n^2)

    #     Args:
    #         grid (List[List[int]]): each cell in the grid is either 0(empty) or 1

    #     Returns:
    #         int: the shortest path to go 8-directionally from (0,0) to (n-1,n-1)
    #     """

    #     n = len(grid)
    #     EMPTY = 0
    #     k = 1
    #     queue = [(0, 0, k)]
    #     dirs = [(1, -1), (1, 0), (1, 1), (0, 1),
    #             (-1, 1), (-1, 0), (-1, -1), (0, -1)]

    #     if grid[0][0] != EMPTY or grid[n-1][n-1] != EMPTY:
    #         return -1

    #     def valid(y: int, x: int) -> tuple:
    #         for r, c in dirs:
    #             r += y
    #             c += x
    #             if 0 <= r < n and 0 <= c < n and grid[r][c] == EMPTY:
    #                 yield(r, c)
    #         return (-1, -1)

    #     while queue:
    #         y, x, k = queue.pop(0)
    #         if y == n-1 and x == n-1:
    #             return k
    #         for r, c in valid(y, x):
    #             grid[r][c] = 1
    #             queue.append((r, c, k+1))
    #     return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """ Strategey 1: BFS
        Runtime: O(n^2 Log(n^2)), where n is the # of rows
        Space: O(n^2)


        Args:
            grid (List[List[int]]): each cell in the grid is either 0(empty) or 1       

        Returns:
            int: the shortest path to go 8-directionally from (0,0) to (n-1,n-1)
        """

        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        # Helper function for the A* heuristic.
        def best_case_estimate(row, col):
            return max(max_row - row, max_col - col)

        # Check that the first and last cells are open.
        if grid[0][0] or grid[max_row][max_col]:
            return -1

        # Set up the A* search.
        visited = set()
        # Entries on the priority queue are of the form
        # (total distance estimate, distance so far, (cell row, cell col))
        priority_queue = [(1 + best_case_estimate(0, 0), 1, (0, 0))]
        while priority_queue:
            estimate, distance, cell = heapq.heappop(priority_queue)
            if cell in visited:
                continue
            if cell == (max_row, max_col):
                return distance
            visited.add(cell)
            for neighbour in get_neighbours(*cell):
                # The check here isn't necessary for correctness, but it
                # leads to a substantial performance gain.
                if neighbour in visited:
                    continue
                estimate = best_case_estimate(*neighbour) + distance + 1
                entry = (estimate, distance + 1, neighbour)
                heapq.heappush(priority_queue, entry)

        # There was no path.
        return -1

# @lc code=end

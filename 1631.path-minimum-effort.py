from typing import List, Tuple
import math
import heapq


class Solution:

    # def minimumEffortPath(self, heights: List[List[int]]) -> int:
    #     """Strategy 1: Dijkstra
    #     Runtime: O(n * m * log(n*m)), where n is the # of rows and m is the # of cols
    #     Space: O(n *m)

    #     Args:
    #         heights (List[List[int]]): the height board

    #     Returns:
    #         int: minimum effort to travel from (0,0) to (n01,m-1)

    #     Yields:
    #         Iterator[int]: row,col
    #     """
    #     n = len(heights)
    #     m = len(heights[0])

    #     diff_mat = [[math.inf] * m for _ in range(n)]
    #     diff_mat[0][0] = 0
    #     visited = [[False] * m for _ in range(n)]
    #     heap = [(0, 0, 0)]

    #     def valid(y: int, x: int) -> Tuple[int, int]:
    #         for r, c in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
    #             if 0 <= r < n and 0 <= c < m and not visited[r][c]:
    #                 yield (r, c)
    #         return (-1, -1)

    #     while heap:
    #         diff, y, x = heapq.heappop(heap)
    #         visited[y][x] = True
    #         for r, c in valid(y, x):
    #             curr_diff = abs(heights[r][c] - heights[y][x])
    #             max_diff = max(curr_diff, diff_mat[y][x])
    #             if diff_mat[r][c] > max_diff:
    #                 diff_mat[r][c] = max_diff
    #                 heapq.heappush(heap, (max_diff, r, c))
    #     return diff_mat[-1][-1]

    # def minimumEffortPath(self, heights: List[List[int]]) -> int:
    #     """Strategy 2:Disjoint Set
    #     Runtime: O(n * m * log(n*m)), where n is the # of rows and m is the # of cols
    #     Space: O(n *m)

    #     Args:
    #         heights (List[List[int]]): the height board

    #     Returns:
    #         int: minimum effort to travel from (0,0) to (n01,m-1)
    #     """
    #     class UnionFind:
    #         def __init__(self, size):
    #             self.parent = [x for x in range(size)]
    #             self.rank = [0]*(size)

    #         def find(self, i):
    #             if self.parent[i] != i:
    #                 self.parent[i] = self.find(self.parent[i])
    #             return self.parent[i]

    #         def union(self, x, y):
    #             parent_x = self.find(x)
    #             parent_y = self.find(y)
    #             if parent_x != parent_y:
    #                 if self.rank[parent_x] > self.rank[parent_y]:
    #                     self.parent[parent_y] = parent_x
    #                 elif self.rank[parent_x] < self.rank[parent_y]:
    #                     self.parent[parent_x] = parent_y
    #                 else:
    #                     self.parent[parent_y] = parent_x
    #                     self.rank[parent_x] += 1

    #     row = len(heights)
    #     col = len(heights[0])
    #     if row == 1 and col == 1:
    #         return 0

    #     edge_list = []
    #     for current_row in range(row):
    #         for current_col in range(col):
    #             if current_row > 0:
    #                 difference = abs(
    #                     heights[current_row][current_col] -
    #                     heights[current_row - 1][current_col])
    #                 edge_list.append(
    #                     (difference, current_row * col + current_col,
    #                      (current_row - 1) * col + current_col))
    #             if current_col > 0:
    #                 difference = abs(
    #                     heights[current_row][current_col] -
    #                     heights[current_row][current_col - 1])
    #                 edge_list.append(
    #                     (difference, current_row * col + current_col, current_row
    #                      * col + current_col - 1))
    #     edge_list.sort()
    #     union_find = UnionFind(row*col)

    #     for difference, x, y in edge_list:
    #         union_find.union(x, y)
    #         if union_find.find(0) == union_find.find(row*col-1):
    #             return difference
    #     return -1

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """Strategy 2:Disjoint Set 
        Runtime: O(n * m, where n is the # of rows and m is the # of cols
        Space: O(n *m)

        Args:
            heights (List[List[int]]): the height board

        Returns:
            int: minimum effort to travel from (0,0) to (n01,m-1)
        """

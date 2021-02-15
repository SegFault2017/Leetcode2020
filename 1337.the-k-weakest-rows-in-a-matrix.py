#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#


import heapq
from itertools import product
# @lc code=start


class Solution:
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     """ Strategey 1: Binary Search + Heap
    #     Runtime: O(n * log(m *k))
    #     Space：O(k)

    #     Args:
    #         mat (List[List[int]]): each cell either contain 0 or 1 with all ones
    #         always stand in the frontier of a row
    #         k (int): a non-negative integer

    #     Returns:
    #         List[int]: list of indices of the first k weakest row
    #     """

    #     n = len(mat)
    #     m = len(mat[0])

    #     def binary_search(row: int) -> int:
    #         low, high = 0, m
    #         while low < high:
    #             mid = low + (high - low) // 2
    #             if row[mid] == 1:
    #                 low = mid+1
    #             else:
    #                 high = mid
    #         return low

    #     pq = []
    #     for i, row in enumerate(mat):
    #         strength = binary_search(row)
    #         entry = (-strength, -i)
    #         if len(pq) < k or entry > pq[0]:
    #             heapq.heappush(pq, entry)
    #         if len(pq) > k:
    #             heapq.heappop(pq)

    #     indices = []
    #     while pq:
    #         indices.append(-heapq.heappop(pq)[1])
    #     return indices[::-1]

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """ Strategey 1: Binary Search + Heap
        Runtime: O(n * m), where n is the # of rows, m is the # of cols
        Space：O(1)


        Args:
            mat (List[List[int]]): each cell either contain 0 or 1 with all ones 
            always stand in the frontier of a row
            k (int): a non-negative integer

        Returns:
            List[int]: list of indices of the first k weakest row
        """

        indices = []
        n = len(mat)
        m = len(mat[0])

        for c, r in product(range(m), range(n)):
            if len(indices) == k:
                break
            if mat[r][c] == 0 and (c == 0 or mat[r][c-1] == 1):
                indices.append(r)

        i = 0
        while len(indices) < k:
            if mat[i][-1] == 1:
                indices.append(i)
            i += 1
        return indices

        # @lc code=end

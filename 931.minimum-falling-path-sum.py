#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """ Strategey 1: Dynamic Programming
        Runtime: O(n *m), where n is # of rows and m is # of cols
        Space: O(n*m)

        Args:
            matrix (List[List[int]]): each cell in the matrix is an integer

        Returns:
            int: return the minimum falling path
        """
        while len(matrix) >= 2:
            row = matrix.pop()
            n = len(row)
            for i in range(len(row)):
                matrix[-1][i] += min(row[max(0, i-1)],
                                     row[i], row[min(n-1, i+1)])
        return min(matrix[0])
# @lc code=end

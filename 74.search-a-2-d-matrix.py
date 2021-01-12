#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ Strategy 1: Binary Search
        Runtime: O(log(m *n)), where n is the # of rows, m is the # of columns
        Space: O(1)
        Args:
            matrix (List[List[int]]): a 2d array of ints
            target (int): the wanted value

        Returns:
            bool: determined whether target is in matrix
        """

        n = len(matrix)
        if n == 0:
            return False

        m = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left)//2
            pivot = matrix[mid // m][mid % m]
            if target == pivot:
                return True
            elif target < pivot:
                right = mid - 1
            else:
                left = mid + 1
        return False
# @lc code=end

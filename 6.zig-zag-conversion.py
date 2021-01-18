#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """ Strategy 1: Convert by row
        Runtiem: O(n)
        Space:O(n)

        Args:
            s (str): the string to be transformed
            numRows (int): the # of rows

        Returns:
            str: the transfromed string in zig zag pattern
        """

        row = [""] * numRows
        going_down = False
        curr_row = 0

        if (numRows == 1):
            return s

        for c in s:
            row[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                going_down ^= 1
            curr_row += 1 if going_down else -1

        output = ""
        for r in row:
            output += r
        return output

# @lc code=end

#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """ Backtracking
        Runtime: O(n)
        Space: O(n)

        Args:
            n (int): number of parentheses

        Returns:
            List[str]: a list of well-formed parentheses
        """

        output = []

        def backTrack(s="", l=0, r=0) -> None:
            if len(s) == 2*n:
                output.append(s)
                return
            if l < n:
                backTrack(s+"(", l + 1, r)
            if r < l:
                backTrack(s+")", l, r+1)
            return
        backTrack("", 0, 0)
        return output

# @lc code=end

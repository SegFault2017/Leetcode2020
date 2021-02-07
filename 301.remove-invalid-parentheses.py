#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def validParen(self, s: str) -> bool:
        count = 0
        for c in s:
            count += (c == self.left_P)
            count -= (c == self.right_p)
            if count < 0:
                return False
        return count == 0

    def dfs(self, s: str, start: int, left: int, right: int) -> None:
        if left == 0 and right == 0 and self.validParen(s):
            self.output.append(s)
            return

        n = len(s)
        for i in range(start, n):
            if i != start and s[i] == s[i-1]:
                continue

            if right > 0 and s[i] == self.right_p:
                temp = s[:i] + s[i+1:]
                self.dfs(temp, i, left, right-1)
            elif left > 0 and s[i] == self.left_P:
                temp = s[:i] + s[i+1:]
                self.dfs(temp, i, left-1, right)
        return

    def removeInvalidParentheses(self, s: str) -> List[str]:
        """ Strategy 1: Backtrack
        Runtime:O(2^(l+r)), where l is the # of unbalanced (, r is the #  of unbalanced)
        Spacetime:O(2^(l+r))

        Args:
            s (str): the string s

        Returns:
            List[str]: all possible valid parenthese
        """
        if not s:
            return [""]
        left = right = 0
        self.left_P = "("
        self.right_p = ")"
        self.output = []

        for c in s:
            left += (c == self.left_P)
            if left == 0:
                right += (c == self.right_p)
            else:
                left -= (c == self.right_p)

        self.dfs(s, 0, left, right)
        return self.output

        # count # of unbalanced parenthese


# @lc code=end

#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
from typing import Pattern


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """ Strategy 1: Dynamic Programming
        Runtime: O(n * m), where n is the length of s and m is the length of p
        Space: O(n * m)

        Args:
            s (str): the string to be matched
            p (str): the pattern

        Returns:
            bool: determine whether s can be matched by p
        """


# @lc code=end

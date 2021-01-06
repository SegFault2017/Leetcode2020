#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """ Strategy 1: Stack
        Runtime: O(n)
        Sapce:O(n)

        Args:
            s (str): the parentheses string

        Returns:
            bool: determine whether s is the valid parentheses
        """

        stack = []
        cache = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in cache:
                top = stack.pop() if stack else '#'
                if top != cache[c]:
                    return False
            else:
                stack.append(c)
        return not stack
# @lc code=end

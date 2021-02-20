#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """ Strategy 1: Stack
        Runtime: O(n), where n is length of s
        Space: O(n)

        Args:
            s (str): a string consists of round brackets and lowercase letters

        Returns:
            str: string with valid round brackets
        """

        stack = []
        CLOSING = ")"
        OPENING = "("
        idx2Remove = set()

        for i, c in enumerate(s):
            if c != CLOSING and c != OPENING:
                continue
            if c == OPENING:
                stack.append(i)
            elif not stack:
                idx2Remove.add(i)
            else:
                stack.pop()

        idx2Remove = idx2Remove.union(set(stack))

        output = ""
        for i, c in enumerate(s):
            if i not in idx2Remove:
                output += c
        return output


# @lc code=end

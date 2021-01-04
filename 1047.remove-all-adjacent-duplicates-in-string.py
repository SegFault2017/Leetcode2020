#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        """ Stack
        Runtime: O(n), where n is the length of S
        Space: O(n)

        Args:
            S (str): the string S

        Returns:
            str: the modified string S, where it does not have adjacent dupilcates
        """

        stack = []
        i = 0
        n = len(S)

        while i < n:
            if not stack or stack[-1] != S[i]:
                stack.append(S[i])
            else:
                stack.pop()
            i += 1
        return "".join(stack)

# @lc code=end

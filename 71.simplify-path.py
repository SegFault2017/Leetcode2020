#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        """ Strategy 1: Stack

        Args:
            path (str): path starting from root directory

        Returns:
            str: simplified version of the canonical path
        """

        stack = []

        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif not portion or portion == ".":
                continue
            else:
                stack.append(portion)
        return "/" + "/".join(stack)
# @lc code=end

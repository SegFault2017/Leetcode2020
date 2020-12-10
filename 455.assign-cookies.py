#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """Strategy 1: Assign cookies

        Args:
            g (List[int]): list of greed factor
            s (List[int]): list of cookie size

        Returns:
            int: the maximum of content children
        """

        if not s:
            return 0

        i = j = 0
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        cookies = 0

        while i < n and j < m:
            if s[j] >= g[i]:
                i += 1
                j += 1
                cookies += 1
            else:
                j += 1
        return cookies
# @lc code=end

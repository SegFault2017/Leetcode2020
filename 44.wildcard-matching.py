#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
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

        s_len = len(s)
        p_len = 0
        pattern = list(p)
        isFirst = True

        for _, c in enumerate(p):
            if c == "*":
                if isFirst:
                    pattern[p_len] = c
                    p_len += 1
                    isFirst = False
            else:
                pattern[p_len] = c
                p_len += 1
                isFirst = True

        dp = [[False] * (p_len+1) for _ in range(s_len+1)]
        dp[0][0] = 1

        if s == p or pattern == "*":
            return True

        if p_len > 0 and pattern[0] == "*":
            dp[0][1] = True

        for y in range(1, s_len+1):
            for x in range(1, p_len+1):
                if pattern[x-1] == "?" or s[y-1] == pattern[x-1]:
                    dp[y][x] = dp[y-1][x-1]
                elif pattern[x-1] == "*":
                    dp[y][x] = dp[y-1][x] or dp[y][x-1]

        return dp[s_len][p_len]


# @lc code=end

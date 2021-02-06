#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
from abc import abstractmethod


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """ Strategy 1: Dynamic Programming
        Runtime: O(n * m), where n is the length of s and m is the length of p
        Space: O(n * m)

        Args:
            s (str): the string to be matched
            p (str): a regex pattern

        Returns:
            bool: determine whether s can be matched by p
        """

        s_len = len(s)
        p_len = 0
        isFirst = True
        pattern = list(p)

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

        if s == p or pattern == [".", "*"]:
            return True
        # print(pattern)
        dp = [[False] * (p_len+1) for _ in range(s_len+1)]
        dp[0][0] = 1

        for i in range(2, p_len+1):
            if pattern[i-1] == "*":
                dp[0][i] = dp[0][i-2]

        for y in range(1, s_len+1):
            for x in range(1, p_len+1):
                if pattern[x-1] == "." or s[y-1] == pattern[x-1]:
                    dp[y][x] = dp[y-1][x-1]
                elif pattern[x-1] == "*":
                    dp[y][x] = dp[y][x-2]
                    if pattern[x-2] == "." or pattern[x-2] == s[y-1]:
                        dp[y][x] = dp[y][x] or dp[y-1][x]
        return dp[s_len][p_len]
# @lc code=end

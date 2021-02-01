#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """Strategy 1: Dynamic Programming
        Runtime: O(n^2), where n is the length of s
        Space:O(n^2)

        Args:
            s (str): the string

        Returns:
            int: the longest common subsequence
        """
        n = len(s)
        dp = [[0 if j != i else 1 for j in range(n+1)] for i in range(n+1)]
        dp[0][0] = 0

        for x in range(2, n+1):
            for y in range(x-1, -1, -1):
                if s[y-1] == s[x-1]:
                    dp[y][x] += dp[y+1][x-1] + 2
                else:
                    dp[y][x] = max(dp[y][x-1], dp[y+1][x])
        return dp[1][-1]
# @lc code=end

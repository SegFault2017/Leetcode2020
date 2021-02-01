#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Strategy 1: Dynamic Programming

        Args:
            s (str): The length of the string

        Returns:
            str: the longest palindrome

            a b c
          a 1 
          b   1
          c     1
        """
        n = len(s)
        dp = [[True if y == x else False for x in range(n)] for y in range(n)]
        # dp = [[False] * n for _ in range(n)]
        # dp[0][0] = True
        longest = 1
        start = 0
        for x in range(1, n):
            for y in range(x):
                if s[y] == s[x] and (x == y + 1 or dp[y+1][x-1]):
                    dp[y][x] = True
                    if longest < x - y + 1:
                        longest = x - y + 1
                        start = y
        return s[start: start + longest]


# @lc code=end

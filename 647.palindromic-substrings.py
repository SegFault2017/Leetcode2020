#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        """ Strategy 1: Dynamic Programming
        Runtime: O(n *m)
        Space: O(n*m)


        Args:
            s (str): the string

        Returns:
            int: # of palindrome substring in s
        """
        output = n = len(s)
        dp = [[True if y == x else False for x in range(n)] for y in range(n)]

        for x in range(1, n):
            for y in range(x):
                if s[y] == s[x] and (y + 1 == x or dp[y+1][x-1]):
                    dp[y][x] = True
                    output += 1
        return output

# @lc code=end

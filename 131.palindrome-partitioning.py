#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1

        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        """Strategy 1: BackTrack
        Runtime: O(n * 2 ^n), where n is the length of the string s
        Space: O(n)

        Args:
            s (str): the string

        Returns:
            List[List[str]] : a list of possible palindro partitioning
        """
        temp = []
        output = []

        def dfs(string: str) -> None:
            n = len(string)
            if n == 0:
                output.append(temp[:])
                return

            for i in range(n):
                if self.isPalindrome(string[:i+1]):
                    temp.append(string[:i+1])
                    dfs(string[i+1:])
                    temp.pop()
            return
        dfs(s)
        return output

        # @lc code=end

#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
from typing import List


class Solution:

    def isSubsequence(self, word: str, s: str) -> bool:
        i = j = 0
        n = len(word)
        m = len(s)

        while i < n and j < m:
            if s[j] == word[i]:
                i += 1
            j += 1
        return i == n

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """ Strategy 1: subsequence comparison
        Runtime: O(n *m), where n is # of words in d, 
        and m is the length of the longest word in d
        Space: O(m)

        Args:
            s (str): the string s
            d (List[str]): list of words in dictionary

        Returns:
            str: the smallest longest word in d
        """

        if not s or not d:
            return ""

        longest = ""
        for word in d:
            n = len(word)
            if self.isSubsequence(word, s):
                if n > len(longest):
                    longest = word
                elif n == len(longest) and word < longest:
                    longest = word
        return longest

        # @lc code=end

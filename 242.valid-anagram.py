#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
from collections import Counter

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ Hash
        Runtime: o(max(s,t)), where n is the length of s and m is the length of t
        Space: O(n + m)

        Args:
            s (str): the string s
            t (str): the string t

        Returns:
            bool: determine whether s is a string of t
        """

        if len(s) != len(t):
            return False

        counter = Counter(s)

        for c in t:
            if c not in t:
                return False
            counter[c] -= 1
            if counter[c] < 0:
                return False
        return True


# @lc code=end

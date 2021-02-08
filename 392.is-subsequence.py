#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """ Stretegey 1: 2 pointers
        Runtime: O(n), where n is the length of s 

        Args:
            s (str): the string s
            t (str): the string t

        Returns:
            bool: determine whether s is a subsequence of t
        """

        s_len = len(s)
        t_len = len(t)

        if not s:
            return True
        if s_len > t_len:
            return False

        i = j = 0
        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == s_len


# @lc code=end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Strategy 2: Sliding window optimized
        Rutime: O(n)
        Space: O(min(m,n)), where m is the size of the charset and n is the length of the string

        Args:
            s (str): a string

        Returns:
            int: the length of the longest substring without duplicates characters.
        """
        n = len(s)
        if n == 0:
            return 0
        char_set = {}
        i = longest = 0
        for index, c in enumerate(s):
            if c in char_set:
                i = max(char_set[c], i)
            char_set[c] = index+1
            longest = max(longest, index - i + 1)
            # print(i, index, char_set)

        return longest

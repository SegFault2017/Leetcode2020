#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        output = 0
        for count in counter.values():
            output += count // 2 * 2
            if output % 2 == 0 and count % 2 == 1:
                output += 1
        return output
# @lc code=end

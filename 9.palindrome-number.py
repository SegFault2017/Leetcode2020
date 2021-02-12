#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
from abc import abstractmethod


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ Strategey 1: reverse half
        Runtime: O(log(n)) base 10
        Space: O(1)


        Args:
            x (int): an integer

        Returns:
            bool: determine whether x is a palindrome number
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        while x > reverse:
            reverse = 10 * reverse + x % 10
            x //= 10
        return x == reverse or x == reverse//10


# @lc code=end

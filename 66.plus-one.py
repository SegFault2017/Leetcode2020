#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Strtegy 1: Iterative
        Runtime: O(n), where n is the number of digits
        Space: O(1)
        Args:
            digits (List[int]): list of digits

        Returns:
            List[int]: list of digits after added one
        """
        n = len(digits)
        if digits[0] == 0:
            digits[n-1] = 1
            return digits
        not_nine = 0
        for i in range(n):
            if digits[i] != 9:
                not_nine = i

        digits[not_nine] = (digits[not_nine] + 1) % 10
        not_nine += 1
        while not_nine < n:
            digits[not_nine] = 0
            not_nine += 1

        return digits if digits[0] != 0 else [1] + digits


# @lc code=end

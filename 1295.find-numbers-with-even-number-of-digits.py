#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def calDigits(self, num: int) -> int:
        count = 0
        while num > 0:
            count += 1
            num //= 10
        return count

    def findNumbers(self, nums: List[int]) -> int:
        """ Strategey 1: One Pass
        Runtime: O(n)
        Space:O(1)

        Args:
            nums (List[int]): a list of non-negative integers

        Returns:
            int: the # of numbers which has even numbers of digits.
        """

        count = 0
        for num in nums:
            if self.calDigits(num) % 2 == 0:
                count += 1
        return count

# @lc code=end

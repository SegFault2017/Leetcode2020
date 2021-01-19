#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number(self, num: int) -> int:
        """ Strategy 1: Brute Force
        Runtime: O(n)
        Space:O(1)

        Args:
            num (int): an integer onlhy consists of 6's and 9's

        Returns:
            int: maximum number consisting only 6's and 9's
        """

        temp = list(str(num))

        for i in range(len(temp)):
            if temp[i] == "6":
                temp[i] = "9"
                return "".join(temp)
        return num


# @lc code=end

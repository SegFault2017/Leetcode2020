#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """ Strategy 1: Binary search
        Runtime: O(log (num))
        Space: O(1) 

        Args:
            num (int): a non-negative integer   

        Returns:
            bool: determine whether number is a perfect square.
        """

        if num < 2:
            return True

        lo, hi = 0, num//2

        while lo <= hi:
            mid = lo + (hi - lo)//2
            x = mid**2
            if x == num:
                return True
            elif x < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
# @lc code=end

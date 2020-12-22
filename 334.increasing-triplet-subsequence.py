#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

import math
# @lc code=start


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Strategy 1: Linear scan

        Args:
            nums (List[int]): a list of integers

        Returns:
            bool: determine wherther there exist a increasing subsequence or not.
        """
        first = second = math.inf
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False

# @lc code=end

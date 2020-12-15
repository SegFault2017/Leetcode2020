#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Strategy 2: 2 pointers
        Runtime: O(n), where n is the number of integers in nums
        Space: O(n)
        Args:
            nums (List[int]): a list of non-decreasing integers

        Returns:
            List[int]: a list of non-decreasing sqaured integers
        """

        lo, hi = 0, len(nums) - 1
        output = deque()
        while lo <= hi:
            lo_2 = nums[lo] ** 2
            hi_2 = nums[hi] ** 2
            if lo_2 < hi_2:
                output.appendleft(hi_2)
                hi -= 1
            else:
                output.appendleft(lo_2)
                lo += 1
        return output
# @lc code=end

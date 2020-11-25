#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Strategy 1; Dynamic Programming
        Runtime: O(n), where n is the number of elements in nums
        Space: O(1)
        Hint : Multiplying a min val could give us a maximal.

        Args:
            nums (List[int]): [description]

        Returns:
            int: [description]
        """
        n = len(nums)
        if n == 0:
            return 0

        output = max_prod = min_prod = nums[0]

        for i in range(1, n):
            maximal = max_prod * nums[i]
            minimal = min_prod * nums[i]
            max_prod = max(nums[i], maximal, minimal)
            min_prod = min(nums[i], maximal, minimal)
            output = max(max_prod, output)
        return output
# @lc code=end

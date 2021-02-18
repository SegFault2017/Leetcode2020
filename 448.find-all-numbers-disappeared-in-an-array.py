#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """ Strategey 1: Negate by visitng
        Runtime: O(n), where n is the size of nums
        Space: O(1) 

        Args:
            nums (List[int]): list of integers

        Returns:
            List[int]: list of missing numbers
        """

        n = len(nums)
        output = []

        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        for i in range(n):
            if nums[i] > 0:
                output.append(i+1)
        return output

        # @lc code=end

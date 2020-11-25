#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     """Strategy 1: Dynamic Programming
    #         Runtime: O(n)
    #         Space: O(1)

    #     Args:
    #         nums (List[int]): list of integers

    #     Returns:
    #         int: maximum sum of subarray
    #     """

    #     n = len(nums)
    #     if n == 0:
    #         return 0
    #     max_sum = nums[0]

    #     for i in range(1, n):
    #         if nums[i-1] > 0:
    #             nums[i] = nums[i-1] + nums[i]
    #         max_sum = max(nums[i], max_sum)
    #     return max_sum

    def maxCross(slef, nums: List[int], split: int, start: int, end: int) -> int:
        left_max = nums[split]
        right_max = nums[split+1]
        temp = 0
        for l in range(split, start-1, -1):
            temp += nums[l]
            left_max = max(temp, left_max)

        temp = 0
        for r in range(split+1, end+1):
            temp += nums[r]
            right_max = max(temp, right_max)

        return left_max + right_max

    def maxSubArray(self, nums: List[int]) -> int:
        """Strategy 2: Divide and Conquer
        Runtime: O(n log n), where n is the number of elements
        Space: O(1)

        Args:
            nums (List[int]):  list of integer

        Returns:
            int: maximum sum of subarray
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        split = (n-1)//2
        left_max = self.maxSubArray(nums[:split+1])
        right_sum = self.maxSubArray(nums[split+1:])
        cross_sum = self.maxCross(nums, split, 0, n-1)
        return max(left_max, right_sum, cross_sum)

# @lc code=end

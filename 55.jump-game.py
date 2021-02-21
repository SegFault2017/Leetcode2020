#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

from typing import List


# @lc code=start
class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     """ Strategey 1: Backward + DP/Greedy
    #     Runtime: O(n), where n is  # of integers in nums
    #     Space:(1)

    #     Args:
    #         nums (List[int]): list of non-negative integers

    #     Returns:
    #         bool: determine whether you can jump from index 0 to index n -1
    #     """

    # n = len(nums)
    # target = n-1

    # if nums[0] > target:
    #     return True

    # for i in range(target-1, -1, -1):
    #     if nums[i] + i >= target:
    #         target = i
    # return target == 0

    def canJump(self, nums: List[int]) -> bool:
        """ Strategey 1: Forward + DP/Greedy 
        Runtime: O(n), where n is  # of integers in nums
        Space:(1)

        Args:
            nums (List[int]): list of non-negative integers 

        Returns:
            bool: determine whether you can jump from index 0 to index n -1
        """

        n = len(nums)
        maxPos = nums[0]

        for i in range(1, n):
            if maxPos < i:
                return False
            maxPos = max(maxPos, nums[i] + i)
        return True


# @lc code=end

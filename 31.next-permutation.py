#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List


class Solution:
    def reverse(self, nums: List[int]) -> None:
        i, j = 0, len(nums)-1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Strategey 1: Linear Scan, 2 pointers
        Runtime: O(n), where n is the length of nums
        Space: O(1)
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        i, j = size-2, size - 1

        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i < 0:
            # self.reverse(nums)
            nums[:] = nums[:][::-1]
            return

        while j >= i and nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        return


# @lc code=end

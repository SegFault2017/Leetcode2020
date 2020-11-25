#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """ Strategy 1: Sorting
        Runtime: O(n log n), where n is the number of elements in nums

        Args:
            nums (List[int]): list of integers

        Returns:
            int: Maximum product of three integers
        """
        n = len(nums)
        nums.sort()
        return max(nums[n-1] * nums[0] * nums[1], nums[n-1] * nums[n-2] * nums[n-3])
# @lc code=end

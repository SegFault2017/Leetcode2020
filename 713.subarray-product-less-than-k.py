#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """ Strategy 1: Silding Window
        Runtime: O(n)
        Space: O(1)

        Args:
            nums (List[int]): list of integers
            k (int): an integer

        Returns:
            int: the # of combinations of contigous subarray tha sum up < k
        """

        if k <= 1:
            return 0

        left = 0
        prod = 1
        output = 0

        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            output += right - left + 1
        return output

# @lc code=end

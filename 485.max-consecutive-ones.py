#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """ Strategy 1: One Pass
        Runtime: O(n), where n is size of nums
        Space: O(1)

        Args:
            nums (List[int]): a list of integers

        Returns:
            int: the maximum number of consecutive ones
        """

        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)

# @lc code=end

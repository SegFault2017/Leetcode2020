#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    # def findLengthOfLCIS(self, nums: List[int]) -> int:
    #     """ Strategy 1: Dynamic Programming
    #     Runtime: O(n)
    #     Space:O(n)

    #     Args:
    #         nums (List[int]): a list of integers

    #     Returns:
    #         int: the length of the longest continuous increasing subsequence
    #     """

    #     n = len(nums)
    #     if n <= 1:
    #         return n
    #     longest = 1
    #     dp = [1] * n

    #     for i in range(1, n):
    #         if nums[i-1] < nums[i]:
    #             dp[i] = dp[i-1] + 1
    #         longest = max(longest, dp[i])
    #     return longest

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """ Strategy 1: sliding window
        Runtime: O(n)
        Space:O(1)

        Args:
            nums (List[int]): a list of integers    

        Returns:
            int: the length of the longest continuous increasing subsequence
        """
        n = len(nums)
        if n <= 1:
            return n

        anchor = longest = 0
        for i in range(n):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            longest = max(longest, i - anchor + 1)
        return longest


# @lc code=end

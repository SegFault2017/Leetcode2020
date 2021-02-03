#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


import bisect

# @lc code=start


class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     """ Strategy 1: Dynamic Programming
    #     Runtime: O(n^2), where n is the size of num
    #     Space:O(n)

    #     Args:
    #         nums (List[int]): list of integers

    #     Returns:
    #         int: the length of the longest subsequence
    #     """

    #     if not nums:
    #         return 0

    #     n = len(nums)
    #     dp = [1] * n
    #     longest = 1

    #     for j in range(1, n):
    #         for i in range(j):
    #             if nums[i] < nums[j]:
    #                 dp[j] = max(dp[i]+1, dp[j])
    #         longest = max(longest, dp[j])
    #     return longest

    def lengthOfLIS(self, nums: List[int]) -> int:
        """ Strategy 2: Patience sort
        Runtime: O(n log(n)), where n is the size of num
        Space:O(n)

        Args:
            nums (List[int]): list of integers      

        Returns:
            int: the length of the longest subsequence
        """

        if not nums:
            return 0

        output = []

        for num in nums:
            if not output or num > output[-1]:
                output.append(num)
            else:
                idx = bisect.bisect_left(output, num)
                output[idx] = num
        return len(output)

        # @lc code=end

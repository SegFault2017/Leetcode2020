#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """ Strategy 1: Dynamic Programming
        Runtime: O(n^2)
        Space: O(n)

        Args:
            nums (List[int]): list of integers

        Returns:
            int: # of the longest increasing subsequence
        """

        n = len(nums)
        if n <= 1:
            return n

        dp = [1] * n
        counter = [1] * n

        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if dp[i] >= dp[j]:
                        dp[j] = dp[i] + 1
                        counter[j] = counter[i]
                    elif dp[i] + 1 == dp[j]:
                        counter[j] += counter[i]
        longest = max(dp)
        return sum(count for i, count in enumerate(counter) if dp[i] == longest)
# @lc code=end

#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#


import bisect

# @lc code=start


class Solution:
    # def findNumberOfLIS(self, nums: List[int]) -> int:
    #     """ Strategy 1: Dynamic Programming
    #     Runtime: O(n^2)
    #     Space: O(n)

    #     Args:
    #         nums (List[int]): list of integers

    #     Returns:
    #         int: # of the longest increasing subsequence
    #     """

    #     n = len(nums)
    #     if n <= 1:
    #         return n

    #     dp = [1] * n
    #     counter = [1] * n

    #     for j in range(1, n):
    #         for i in range(j):
    #             if nums[i] < nums[j]:
    #                 if dp[i] >= dp[j]:
    #                     dp[j] = dp[i] + 1
    #                     counter[j] = counter[i]
    #                 elif dp[i] + 1 == dp[j]:
    #                     counter[j] += counter[i]
    #     longest = max(dp)
    #     return sum(count for i, count in enumerate(counter) if dp[i] == longest)

    def findNumberOfLIS(self, nums: List[int]) -> int:
        """ Strategy 1: Dynamic Programming
        Runtime: O(n log(n))
        Space: O(n)

        Args:
            nums (List[int]): list of integers

        Returns:
            int: # of the longest increasing subsequence
        """

        n = len(nums)

        if not n:
            return 0

        end_decks = []
        decks = []
        paths = []
        deck_idx = 0

        for num in nums:
            deck_idx = bisect.bisect_left(end_decks, num)
            n_paths = 1

            if deck_idx > 0:
                l = bisect.bisect(decks[deck_idx-1], -num)
                n_paths = paths[deck_idx-1][-1] - paths[deck_idx-1][l]

            if deck_idx == len(end_decks):
                end_decks.append(num)
                decks.append([-num])
                paths.append([0, n_paths])
            else:
                end_decks[deck_idx] = num
                decks[deck_idx].append(-num)
                paths[deck_idx].append(n_paths + paths[deck_idx][-1])

        return paths[-1][-1]

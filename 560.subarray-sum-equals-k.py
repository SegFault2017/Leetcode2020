#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict


class Solution:
    from collections import defaultdict

    def subarraySum(self, nums: List[int], k: int) -> int:
        """ Strategy 1: Cumulative Sum with Hash
        Runtime: O(N)
        Space: O(N)

        Args:
            nums (List[int]): a list of integers
            k (int): the target integer

        Returns:
            int: # of contigous subarrya that sums up to k
        """

        n = len(nums)
        if n == 0:
            return 0

        counter = defaultdict(int)
        counter[0] = 1
        output = cumulative = 0

        for x in nums:
            cumulative += x
            # if cumulative - k in counter:
            #     output += counter[cumulative - k]
            output += counter[cumulative - k]
            counter[cumulative] += 1
            # if cumulative not in counter:
            #     counter[cumulative] = 1
            # else:
            #     counter[cumulative] += 1
            # if cumulative == k:
            #     output += 1
            # output += counter[cumulative - k]
            # counter[cumulative] += 1
        return output

# @lc code=end

#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """ Startegy 1:Hashmap, similar to 2 sum problem
        Runtime:O(n), where n is the length of nums
        Space:O(n)

        Args:
            nums (List[int]): list of integers      

        Returns:
            int: the length of the longest subsequence
        """

        cache = defaultdict(int)
        longest = 0

        for num in nums:
            cache[num] += 1
            up, down = num + 1, num - 1
            if up in cache:
                longest = max(longest, cache[up] + cache[num])
            if down in cache:
                longest = max(longest, cache[down] + cache[num])

        return longest


# @lc code=end

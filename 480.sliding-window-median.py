#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
from typing import List
import bisect


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """ Strategy 1: Insertion sort
        Runtime: O((n-k)* k)

        Args:
            nums (List[int]): list of integers 
            k (int): window size

        Returns:
            List[float]: list of medians of all (n-k+1) windows with sized k.
        """

        if not nums:
            return []

        if k == 1:
            return nums
        n = len(nums)
        window = nums[:k]
        window.sort()
        medians = []

        for i in range(k, n+1):
            medians.append((window[k//2] + window[(k-1)//2])/2)
            if i == n:
                break
            idx = bisect.bisect_left(window, nums[i-k])
            window.pop(idx)
            bisect.insort_left(window, nums[i])
        return medians
        # @lc code=end

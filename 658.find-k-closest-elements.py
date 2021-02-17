#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
from typing import List


class Solution:
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     """Strategy 1: Sorting by Distance
    #     Runtime: O(n log n), where n is the size of arr
    #     Space:O(n log n)
    #     Args:
    #         arr (List[int]):
    #         k (int): a non-negative integer
    #         x (int): the reference number

    #     Returns:
    #         List[int]: a list of k closest integers to x
    #     """
    #     return sorted(sorted(arr, key=lambda num: (abs(num - x), num))[:k])

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """Strategy 1: Sorting by Distance
        Runtime: O(log(n - k)), where n is the size of arr
        Space:O(1)
        Args:
            arr (List[int]):
            k (int): a non-negative integer
            x (int): the reference number

        Returns:
            List[int]: a list of k closest integers to x
        """

        n = len(arr)
        lo, hi = 0, n-k
        while lo < hi:
            mid = lo + (hi - lo)//2
            if x - arr[mid] > arr[mid+k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]

    # @lc code=end

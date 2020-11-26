#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int, left: bool) -> int:
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = lo // 2 + hi // 2
            if nums[mid] > target or (left and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Strtegy 1: Binary Search
        Runtime: O(log n), where n is the length of the list
        Space: O(1)

        Args:
            nums (List[int]): list of integers
            target (int): the target value

        Returns:
            List[int]: [start, end], where start is an index of the first occurance 
            target and end is the last occurance of target.
        """

        left = self.binary_search(nums, target, True)
        # print(left)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, self.binary_search(nums, target, False)-1]


# @lc code=end

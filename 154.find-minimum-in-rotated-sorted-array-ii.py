#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ Strategy 1: Binary Search
        Runtime: O(log(n)), where n is the size of nums
        Space: O(1)

        Args:
            nums (List[int]): a list of integers

        Returns:
            int: the minimum value of nums
        """

        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]
        # @lc code=end

#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ Strategy1: Binary search
        Runtime: O(log(n)), where n is the number of elements in nums
        Space:O(1)

        Args:
            nums (List[int]): list of integers

        Returns:
            int: return the minimum value in nums
        """

        n = len(nums)
        lo, hi = 0, n-1

        while lo < hi:
            mid = lo + (hi - lo)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

# @lc code=end

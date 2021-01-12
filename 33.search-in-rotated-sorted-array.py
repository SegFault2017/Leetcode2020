#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ Strategy1 : Binary Search
        Runtime: O(log n), where n is the size of nums
        Space: O(1)

        Args:
            nums (List[int]): a list of rotated sorted array
            target (int): the target value

        Returns:
            int: the index of the target value. Otherwise, return -1
        """

        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        start = left
        left, right = 0, n - 1

        if nums[start] <= target <= nums[right]:
            left = start
        else:
            right = start

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
# @lc code=end

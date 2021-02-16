#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ Strategey 1: Binary search
        Runtime: O(log n), where n is the size of nums

        Args:
            nums (List[int]): a list of integers
            target (int): the target value 

        Returns:
            int: index of the target value. reutrn -1 if not found
        """

        n = len(nums)
        low, high = 0, n

        while low < high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return -1

# @lc code=end

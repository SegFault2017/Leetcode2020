#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Strategy 1: 2 Pointers
        Runtime: O(n), where n is the length of the list

        Args:
            nums (List[int]): a list of integers

        Returns:
            int: the length of the modified nums
        """
        n = len(nums)
        j = count = 1

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1

            if count < 3:
                nums[j] = nums[i]
                j += 1
        return j


# @lc code=end

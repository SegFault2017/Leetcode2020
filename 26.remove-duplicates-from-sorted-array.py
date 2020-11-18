#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n

        first_ptr = 0
        second_ptr = 1

        while second_ptr < n:
            if nums[second_ptr] != nums[first_ptr]:
                first_ptr += 1
                nums[first_ptr] = nums[second_ptr]
            second_ptr += 1

        nums = nums[:first_ptr+1]
        return len(nums)
        # @lc code=end

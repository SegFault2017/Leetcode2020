#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Startegy 1: Pointers
        Runtime: O(N)
        Space: O(1)

        Args:
            nums (List[int]): list of integers
        """
        n = len(nums)
        curr = p0 = 0
        p2 = n-1

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
        return


# @lc code=end

#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """ Strategy 1: Sorting
        Runtime: O(n log n)
        Space: O(n)

        Args:
            heights (List[int]): a list of non negative integers

        Returns:
            int: the minimum # of student that must move in order
        """

        return sum((list(h != sh for h, sh in zip(heights, sorted(heights)))))
# @lc code=end

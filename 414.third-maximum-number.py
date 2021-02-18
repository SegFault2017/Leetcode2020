#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """ Strategey 1: Set
        Runtime:O(n)
        Space: O(1)

        Args:
            nums (List[int]): list of integers

        Returns:
            int: third maximum number
        """

        maxSet = set()

        for x in nums:
            maxSet.add(x)
            if len(maxSet) > 3:
                maxSet.remove(min(maxSet))
        # print(maxSet)
        if len(maxSet) == 3:
            return min(maxSet)
        return max(maxSet)
# @lc code=end

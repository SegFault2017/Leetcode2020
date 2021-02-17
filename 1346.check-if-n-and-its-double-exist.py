#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """ Strategy 1: Hash
        Runtime: O(n), where n is the size of arr
        Space:O(1)`

        Args:
            arr (List[int]): a list of integers

        Returns:
            bool: determine whether there exists a element,j, such that it is a double of value i.
        """

        seen = set()

        for x in arr:
            double = 2*x
            half = x/2
            if double in seen or half in seen:
                return True
            seen.add(x)
        return False

        # @lc code=end

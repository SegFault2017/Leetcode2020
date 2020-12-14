#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
from collections import Counter


class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:
        """Strategy 1: Hash map, similar to 2 sum
        Runtime: O(n), where n is the number of elements in the nums
        Space: O(n)

        Args:
            nums (List[int]):  a list of integers
            k (int): an integer,k

        Returns:
            int: the # of pairs which has diff of k
        """

        counter = Counter(nums)
        output = 0

        for x in counter:
            if k > 0 and x + k in counter:
                output += 1
            elif k == 0 and counter[x] > 1:
                output += 1
        return output


# @lc code=end

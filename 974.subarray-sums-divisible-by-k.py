#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """ Strategy 1: Cumulative Sum with Hash
        Runtime: O(N)
        Space: O(N)


        Args:
            A (List[int]): list of integers
            K (int): target value

        Returns:
            int: # of combinations that has sum divisble by k
        """

        n = len(A)

        if n == 0:
            return 0

        cumulaitve = output = 0
        counter = {}
        counter[0] = 1

        for x in A:
            cumulaitve = (cumulaitve + x) % K
            if cumulaitve not in counter:
                counter[cumulaitve] = 1
            else:
                output += counter[cumulaitve]
                counter[cumulaitve] += 1

        return output

        # @lc code=end

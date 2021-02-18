#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """ Strategey 1: 2 Pointers
        Runtime: O(n), where n is the size of A
        Space: O(1)

        Args:
            A (List[int]): a list of non-negative integers

        Returns:
            List[int]: odd elements follows even elements.
        """

        n = len(A)
        if n < 2:
            return A

        j = 0
        for i in range(n):
            if A[i] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                j += 1
        return A
# @lc code=end

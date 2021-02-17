#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """ Strategy 1: Fast power 
        Runtime: O(log(n))
        Space: O(1)

        Args:
            x (float): a float
            n (int): an integer

        Returns:
            float: x raised to the power n
        """

        N = n
        prod = x
        if N == 0 or x == 1:
            return 1.0
        elif N < 0:
            N = -n
            prod = 1/x

        output = 1
        while N != 1:
            if N % 2 == 0:
                prod *= prod
                N /= 2
            else:
                output *= prod
                N -= 1
        return output * prod

# @lc code=end

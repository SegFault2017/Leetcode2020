#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """Strategy 1: Up to root n
        Space: O(n** 0.5 ),
        Space: O(1)

        Args:
            n (int): the number n
            k (int): the number k   

        Returns:
            int: the kth factor of n
        """

        factors = []
        sqrt_n = int(n ** 0.5)

        for x in range(1, sqrt_n+1):
            if n % x == 0:
                k -= 1
                if k == 0:
                    return x
                factors.append(x)

        if sqrt_n ** 2 == n:
            k += 1
        factors_size = len(factors)
        return n // factors[factors_size - k] if k <= factors_size else -1
# @lc code=end

class Solution:
    def numWays(self, n: int, k: int) -> int:
        """ Strategey 1: Dynamic Programming
        Runtime:O(n)
        Space: O(1)

        Args:
            n (int): a positive integer n
            k (int): a positive integer k < n

        Returns:
            int: number of ways to paint all n fences wiht no same color fences more than 2.
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k*k

        f1, f2 = k, k*k
        for i in range(3, n+1):
            f1, f2 = f2, (f1 + f2) * (k-1)
        return f2

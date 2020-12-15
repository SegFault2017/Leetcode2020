from collections import deque


class Solution(object):

    def quadratic(self, x: int, a: int, b: int, c: int) -> int:
        return a * (x ** 2) + b * x + c

    def sortTransformedArray(self, nums, a, b, c):
        """Strategy 1: 2 pointers + parabola concavity

        Args:
            nums ([type]): a list of integers
            a ([type]): coefficient a
            b ([type]): coefficient b
            c ([type]): coefficient c

        Returns:
            [type]: sorted array
        """
        n = len(nums)
        lo, hi = 0, n - 1
        output = deque()

        while lo <= hi:
            lo_2 = self.quadratic(nums[lo], a, b, c)
            hi_2 = self.quadratic(nums[hi], a, b, c)

            if a >= 0:
                if lo_2 <= hi_2:
                    output.appendleft(hi_2)
                    hi -= 1
                else:
                    output.appendleft(lo_2)
                    lo += 1
            else:
                if lo_2 <= hi_2:
                    output.append(lo_2)
                    lo += 1
                else:
                    output.append(hi_2)
                    hi -= 1
        return output

from typing import List


class Solution:
    def formatRange(self, num1: int, num2: int):
        if num1 == num2:
            return str(num1)
        return str(num1) + "->" + str(num2)

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """Strategy 1: Liner Scan

        Args:
            nums (List[int]): a list of integers
            lower (int): lower bound
            upper (int): upper bound

        Returns:
            List[str]: return a list of ranges of missing numbers
        """
        n = len(nums)

        if n == 0:
            return [self.formatRange(lower, upper)]

        ranges = []
        if nums[0] > lower:
            ranges.append(self.formatRange(lower, nums[0]-1))

        for i in range(1, n):
            if nums[i] - nums[i-1] > 1:
                ranges.append(self.formatRange(nums[i-1]+1, nums[i]-1))

        if nums[n-1] < upper:
            ranges.append(self.formatRange(nums[n-1]+1, upper))
        return ranges

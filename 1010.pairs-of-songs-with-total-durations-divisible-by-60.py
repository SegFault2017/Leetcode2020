#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """Startegy 1: Linear Scan + Modulo Property

        Args:
            time (List[int]): list of seconds

        Returns:
            int: the number of pairs that is divisible by 60
        """

        remainders = defaultdict(int)
        output = 0

        for t in time:
            if t % 60 == 0:
                output += remainders[t % 60]
            else:
                output += remainders[60 - t % 60]
            remainders[t % 60] += 1
        return output


# @lc code=end

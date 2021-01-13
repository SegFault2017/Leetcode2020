#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """ Strategy 1: Greedy
        Runtime: O(n), where n is the size of gass and cost
        Space:O(1)

        Args:
            gas (List[int]): a list of gas stations
            cost (List[int]): a list of costs to travel 

        Returns:
            int: the starting station that can travel around the circuit once in the clockwise direction
        """

        start = i = cur = total = 0
        for g, c in zip(gas, cost):
            total += g - c
            cur += g - c
            if cur < 0:
                cur = 0
                start = i + 1
            i += 1
        return start if total >= 0 else -1
# @lc code=end

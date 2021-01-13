#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
#


from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """ Strategy 1: Boats to save people
        Runtime: O(n), where n is the # of people

        Args:
            people (List[int]): # of people
            limit (int): capacity of the boat

        Returns:
            int: the minimum boats that required to save all people
        """
        if not people:
            return 0
        i, j = 0, len(people) - 1
        people.sort()
        boats = 0
        while i <= j:
            boats += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return boats

# @lc code=end

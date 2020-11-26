#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Strategy 1: TimeStamp + sorting
        Runtime: O(n), where n is the length of the list
        Space: O(n)

        Args:
            trips (List[List[int]]): a list of [p, picking, dropping]
            where p is the # of passenagers to pick up,
            picking - picking location
            dropping - dropping location
            capacity (int): maximum capacity of the vehicle

        Returns:
            bool: whether the vehicle can finish the trip without going backward.\
        """

        time_stamps = []
        for trip in trips:
            time_stamps.append([trip[1], trip[0]])
            time_stamps.append([trip[2], -trip[0]])

        time_stamps.sort()
        picked_up = 0

        for _, passengers in time_stamps:
            picked_up += passengers
            if picked_up > capacity:
                return False
        return True


# @lc code=end

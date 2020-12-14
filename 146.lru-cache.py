#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from typing import OrderedDict


class LRUCache(OrderedDict):
    """Strategy 1: Ordered Map
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        return

    def get(self, key: int) -> int:
        """get the value of a key
        Runtime: O(1)
        Args:
            key (int): the key

        Returns:
            int: return the value
        """

        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
        return

# class LRUCache(OrderedDict):
#     """Strategy 1: Ordered Map
#     """

#     def __init__(self, capacity: int):
#         return

#     def get(self, key: int) -> int:
#         """get the value of a key

#         Args:
#             key (int): the key

#         Returns:
#             int: return the value
#         """

#         return

#     def put(self, key: int, value: int) -> None:
#         return

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)

        # @lc code=end

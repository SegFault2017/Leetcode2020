#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from typing import OrderedDict


# class LRUCache(OrderedDict):
#     """Strategy 1: Ordered Map
#     """

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         return

#     def get(self, key: int) -> int:
#         """get the value of a key
#         Runtime: O(1)
#         Args:
#             key (int): the key

#         Returns:
#             int: return the value
#         """

#         if key not in self:
#             return -1

#         self.move_to_end(key)
#         return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)
#         return

class Node():
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        return


class LRUCache():
    """Strategy 2: Hash + Doubly Linked List
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = Node(-1, -1), Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head
        return

    def _add_node(self, node: Node) -> None:

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
        return

    def _remove_node(self, node: Node) -> None:
        if not node:
            return

        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev
        self.size -= 1
        return

    def _pop_tail(self) -> Node:
        temp = self.tail.prev
        self._remove_node(temp)

        return temp

    def _move2front(self, node: Node) -> None:
        self._remove_node(node)
        self._add_node(node)
        return

    def get(self, key: int) -> int:
        """get the value of a key
        Runtime: O(1)
        Args:
            key (int): the key

        Returns:
            int: return the value
        """
        node = self.cache.get(key)
        if not node:
            return -1
        self._move2front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """add or update key 
        Runtime: O(1)
        Args:
            key (int): the key  
            value (int): the value
        """
        node = self.cache.get(key)
        if not node:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.val = value
            self._move2front(node)
        return

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacisty)
        # param_1 = obj.get(key)
        # obj.put(key, value)

        # @lc code=end

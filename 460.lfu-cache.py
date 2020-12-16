#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
        return


class DLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add2Front(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def removeNode(self, node: Node) -> None:
        if not node:
            return
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev
        self.size -= 1
        return

    def popTail(self) -> Node:
        if self.size == 0:
            return None
        last = self.tail.prev
        self.removeNode(last)
        return last


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.freq_lst = defaultdict(DLinkedList)
        self.min_freq = 0

    def update(self, node: Node) -> None:
        freq = node.freq
        self.freq_lst[freq].removeNode(node)
        if self.min_freq == freq and self.freq_lst[freq].size == 0:
            self.min_freq += 1
            del self.freq_lst[freq]
        node.freq += 1
        self.freq_lst[node.freq].add2Front(node)
        return

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        # print("hi", self.min_freq)
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        node = self.cache.get(key)
        if not node:
            if self.size == self.capacity:
                last = self.freq_lst[self.min_freq].popTail()
                del self.cache[last.key]
                self.size -= 1

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.freq_lst[1].add2Front(new_node)
            self.min_freq = 1
            self.size += 1
        else:
            # print("hello")
            self.update(node)
            node.val = value
        return

        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        # @lc code=end

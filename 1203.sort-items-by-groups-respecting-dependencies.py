#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups Respecting Dependencies
#

# @lc code=start
from collections import defaultdict, deque
import collections


class Node:
    def __init__(self) -> None:
        self.neighs = []  # a list of integers
        self.in_degs = 0


class Solution:
    # Topological sort
    # Runtime: O(N),the number of items
    # Space: O(N), n
    from collections import defaultdict, deque

    def topological_sort(self, g: collections.defaultdict(Node), N: int, edges: int) -> List[int]:
        """Returns a topological sorting of a graph

        Args:
            g (collections.defaultdict): a graph
            N (int): number of items
            edges (int): number og edges in the graph

        Returns:
            [type]: None
        """
        ordered = deque()  # a queue that contains all the source nodes
        sources = set()

        for _id in range(N):
            if g[_id].in_degs == 0:
                sources.add(_id)
                ordered.appendleft(_id)

        while sources:
            source = sources.pop()

            for n in g[source].neighs:
                # remove an edge source -> n
                g[n].in_degs -= 1
                edges -= 1
                if g[n].in_degs == 0:
                    sources.add(n)
                    ordered.appendleft(n)
        return ordered if edges == 0 else None

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        OTHER = -1
        sort_by_group = defaultdict(Node)  # graph
        sort_by_items = defaultdict(Node)  # graph)
        i_degs = 0
        g_degs = 0
        ordered = []

        for i in range(n):
            if group[i] == OTHER:
                group[i] = group_id
                group_id += 1
            for beforeItem in beforeItems[i]:
                if group[beforeItem] != group[i]:
                    sort_by_group[group[i]].neighs.append(group[beforeItem])
                    sort_by_group[group[beforeItem]].in_degs += 1
                    g_degs += 1
                sort_by_items[i].neighs.append(beforeItem)
                sort_by_items[beforeItem].in_degs += 1
                i_degs += 1

        sorted_group = self.topological_sort(sort_by_group, group_id, g_degs)
        sorted_items = self.topological_sort(sort_by_items, n, i_degs)

        if not sorted_group or not sorted_items:
            return []

        g_with_sorted_items = defaultdict(list)
        for item in sorted_items:
            g_with_sorted_items[group[item]].append(item)

        for g in sorted_group:
            for item in g_with_sorted_items[g]:
                ordered.append(item)
        return ordered

# @lc code=end

from collections import defaultdict
from typing import List


class Solution:

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """ Strategy 1: Kill by makeing a tree
        Runtime: O(n), where n is the number of pids
        Space: O(n)

        Args:
            pid (List[int]): list of integers
            ppid (List[int]): list of integers
            kill (int): a target pid    

        Returns:
            List[int]: the subtree of the target
        """
        tree = defaultdict(list)
        ppid_set = set(ppid)
        output = []

        for i, _id in enumerate(ppid):
            tree[_id].append(pid[i])

        def dfs(node_id: int) -> None:
            if node_id not in ppid_set:
                return
            for child in tree[node_id]:
                output.append(child)
                dfs(child)
            return
        output.append(kill)
        dfs(kill)
        return output

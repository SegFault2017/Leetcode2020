#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """ Strategey 1: BFS
        Runtime: O(n), where n is the # of nodes in the graph
        Space: O(n)


        Args:
            graph (List[List[int]]): a list of edge list for each node in the graph

        Returns:
            bool: determine whether graph is bipartite or not
        """

        RED = 0
        n = len(graph)
        color = {}

        def BFS(_id: int) -> bool:
            q = [_id]
            color[_id] = RED

            while q:
                node = q.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = color[node] ^ 1
                        q.append(neighbor)
                    else:
                        if color[neighbor] == color[node]:
                            return False
            return True
        return all(BFS(_id) for _id in range(n) if _id not in color)


# @lc code=end

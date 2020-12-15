class Disjoint:
    def __init__(self, n: int) -> None:
        self.rank = [i for i in range(n)]
        self.size = [1] * n
        self.graphs = n

        return

    def findRank(self, i: int) -> int:
        while i != self.rank[i]:
            i = self.rank[i]
        return i

    def weightedUnion(self, i: int, j: int) -> None:
        i_root = self.findRank(i)
        j_root = self.findRank(j)

        if i_root == j_root:
            return
        elif self.size[i_root] > self.size[j_root]:
            self.rank[j_root] = i_root
            self.size[i_root] += self.size[j_root]
        else:
            self.rank[i_root] = j_root
            self.size[j_root] += self.size[i_root]
        self.graphs -= 1
        return


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Strategy 1: Union Find
        Runtime: O(n), where n is the number of nodes in the graphs
        Space: O(n)
        Args:
            n (int): the number of nodes in the graphs
            edges (List[List[int]]): edges of the graphs

        Returns:
            int: number of undirected graph
        """
        disjoint = Disjoint(n)

        for u, v in edges:
            disjoint.weightedUnion(u, v)

        return disjoint.graphs

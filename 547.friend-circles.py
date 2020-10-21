#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Disjoint:
    def __init__(self, n: int) -> None:
        """constructor

        Args:
            n (int): number of students
        """
        self.rank = [i for i in range(n)]
        self.size = [1] * n
        self.circles = n

    def find_rank(self, i: int) -> int:
        """[finds the rank of the ith person]

        Args:
            i (int): the ith person

        Returns:
            int: the rank/root of the ith person
        """

        while self.rank[i] != i:
            i = self.rank[i]
        return i

    def find(self, i: int, j: int) -> bool:
        """ Determine whether the ith student and the jth sutdent have the same 
        connectivity

        Args:
            i (int): the ith student
            j (int): the jth student

        Returns:
            bool: Are ith and jth connected
        """
        return self.find_rank(i) == self.find_rank(j)

    def weighted_union(self, i: int, j: int) -> None:
        i_root = self.find_rank(i)
        j_root = self.find_rank(j)

        if i_root == j_root:
            return
        if self.size[i_root] < self.size[j_root]:
            self.rank[i_root] = self.rank[j_root]
            self.size[j_root] += self.rank[i_root]
        else:
            self.rank[j_root] = self.rank[i_root]
            self.size[i_root] += self.size[j_root]
        self.circles -= 1


class Solution:
    # Runtime: n * m, where n is the # of rows, m is the # of cols
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        disjoint = Disjoint(n)
        DIRECT = 1

        for i in range(n):
            for j in range(n):
                if M[i][j] == DIRECT:
                    disjoint.weighted_union(i, j)

        return disjoint.circles

# @lc code=end

#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, l: TreeNode, r: TreeNode) -> bool:
        if not l and not r:
            return True
        elif not l:
            return False
        elif not r:
            return False

        if l.val != r.val:
            return False
        return self.dfs(l.right, r.left) and self.dfs(l.left, r.right)

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     """ Strategy 1: DFS
    #     Runtime: O(n), where n is the # of nodes
    #     Space: O(1)

    #     Args:
    #         root (TreeNode): the root of the node

    #     Returns:
    #         bool: determine whether the tree is symmetric around the center.
    #     """
    #     if not root:
    #         return True

    #     return self.dfs(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        """ Strategy 1: Iterative
        Runtime: O(n), where n is the # of nodes
        Space: O(1)

        Args:
            root (TreeNode): the root of the node 

        Returns:
            bool: determine whether the tree is symmetric around the center.
        """

        if not root:
            return True
        q_l = [root]
        q_r = [root]

        while q_l and q_r:
            node_l = q_l.pop(0)
            node_r = q_r.pop(0)

            if not node_l and not node_r:
                continue

            if not node_l or not node_r:
                return False

            if node_l.val != node_r.val:
                return False

            for child in [node_l.left, node_l.right]:
                q_l.append(child)

            for child in [node_r.right, node_r.left]:
                q_r.append(child)

        return True
        # @lc code=end

#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """ Strategy 1: DFS
        Runtime: O(n), where n is the number of nodes in the tree.
        Space: O(h), where h is the height of the tree

        Args:
            inorder (List[int]): node's value in inorder order
            postorder (List[int]): node's value in postorder order.

        Returns:
            TreeNode: a proper binary tree
        """

        n = len(inorder)
        if not n:
            return None

        idx_cache = {val: i for i, val in enumerate(inorder)}

        def dfs(l_idx: int, r_idx: int):
            if l_idx > r_idx:
                return None

            node = postorder.pop()
            root = TreeNode(node)
            idx = idx_cache[node]
            root.right = dfs(idx+1, r_idx)
            root.left = dfs(l_idx, idx-1)
            return root
        return dfs(0, n-1)


# @lc code=end

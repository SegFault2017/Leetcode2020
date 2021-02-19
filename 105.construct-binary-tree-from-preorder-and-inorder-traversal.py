#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """ Strategy 1: dfs
        Runtime: O(n), where n is the number of nodes
        Space:O(h), where h is the height of the tree

        Args:
            preorder (List[int]): nodes ordered in preorder traversal
            inorder (List[int]): nodes ordered in inorder traversal

        Returns:
            TreeNode: the proper binary tree
        """

        n = len(inorder)
        if not n:
            return None

        idx_cache = {val: i for i, val in enumerate(inorder)}

        def dfs(l_idx: int, r_idx: int) -> TreeNode:
            if l_idx == r_idx:
                return None

            node = preorder.pop(0)
            root = TreeNode(node)
            idx = idx_cache[node]

            root.left = dfs(l_idx, idx)
            root.right = dfs(idx + 1, r_idx)
            return root

        return dfs(0, n)
        # @lc code=end

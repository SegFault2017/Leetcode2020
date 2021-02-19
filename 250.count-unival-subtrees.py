# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        """ Strategy 1: Dfs
        Runtime: O(n), where n is the # of nodes
        Space:O(h), where h is the height of the tree

        Args:
            root (TreeNode): the root node

        Returns:
            int: number unival subtree
        """
        if not root:
            return 0

        count = 0

        def dfs(node: TreeNode) -> bool:
            nonlocal count

            if not node.left and not node.right:
                count += 1
                return True

            is_uni = True

            for child in [node.left, node.right]:
                if child:
                    is_uni = dfs(child) and is_uni and child.val == node.val
            count += is_uni
            return is_uni
        dfs(root)
        return count

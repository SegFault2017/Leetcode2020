#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    #     """ Strategy 1: DFS
    #    Runtime: O(h), where h is the height of the tree
    # Space: O(h),

    #     Args:
    #         root (TreeNode): the root node
    #         val (int): the insertion val

    #     Returns:
    #         TreeNode: original tree with inserted node with value as val
    #     """

    #     if not root:
    #         return TreeNode(val)

    #     if root.left:
    #         root.left = self.insertIntoBST(root.left, val)

    #     if root.right:
    #         root.right = self.insertIntoBST(root.right, val)

    #     return root

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """ Strategy 1: DFS
            Runtime: O(h), where h is the height of the tree
            Space: O(h),

            Args:
                root (TreeNode): the root node
                val (int): the insertion val

            Returns:
                TreeNode: original tree with inserted node with value as val
        """

        if not root:
            return TreeNode(val)
        stack = [root]
        cur = root

        while stack:
            node = stack.pop()

            if node.val > val:
                if node.left:
                    stack.append(node.left)
                else:
                    node.left = TreeNode(val)
                    return root
            else:
                if node.right:
                    stack.append(node.right)
                else:
                    node.right = TreeNode(val)
                    return root
        return root


# @lc code=end

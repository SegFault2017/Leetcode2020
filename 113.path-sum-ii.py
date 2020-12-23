#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    #     """ Strategy 1: BackTracking
    #     Runtime: O(n), where n is the number of nodes in the tree
    #     Space: O(h), where h is the height of the tree

    #     Args:
    #         root (TreeNode): the root of the tree
    #         sum (int): the target value

    #     Returns:
    #         List[List[int]]: a list of possible path sum from root to leaves that sums up to the target value.
    #     """

    #     if not root:
    #         return None

    #     paths = []
    #     path = [root.val]

    #     def dfs(node: 'TreeNode', total: int) -> None:
    #         if not node.left and not node.right and total == 0:
    #             paths.append(path[:])
    #             return

    #         for child in [node.left, node.right]:
    #             if child:
    #                 path.append(child.val)
    #                 dfs(child, total - child.val)
    #                 path.pop()
    #         return

    #     dfs(root, sum - root.val)
    #     return paths

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """ Strategy 2: Iterative
        Runtime: O(n), where n is the number of nodes in the tree
        Space: O(h), where h is the height of the tree

        Args:
            root (TreeNode): the root of the tree
            sum (int): the target value

        Returns:
            List[List[int]]: a list of possible path sum from root to leaves that sums up to the target value.
        """

        if not root:
            return None
        paths = []
        path = [root.val]
        stack = [(root, sum - root.val, path)]

        while stack:
            node, total, path = stack.pop()
            if not node.left and not node.right and total == 0:
                paths.append(path)
            else:
                for child in [node.left, node.right]:
                    if child:
                        stack.append(
                            (child, total - child.val, path + [child.val]))

        return paths

    # @lc code=end

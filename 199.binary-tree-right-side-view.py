#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def rightSideView(self, root: TreeNode) -> List[int]:
    #     """ Strategey 1: BFS
    #     Runtime: O(H), where H is the height of the tree
    #     Space: O(H)

    #     Args:
    #         root (TreeNode): the root of the tree

    #     Returns:
    #         List[int]: all the nodes viewed from the right side
    #     """
    #     if not root:
    #         return []
    #     cur_lvl = []
    #     nxt_lvl = [root]
    #     output = []

    #     while nxt_lvl:
    #         output.append(nxt_lvl[-1].val)
    #         cur_lvl = nxt_lvl
    #         nxt_lvl = []
    #         while cur_lvl:
    #             node = cur_lvl.pop(0)
    #             for child in [node.left, node.right]:
    #                 if child:
    #                     nxt_lvl.append(child)
    #     return output

    def rightSideView(self, root: TreeNode) -> List[int]:
        """ Strategey 1: DFS
        Runtime: O(H), where H is the height of the tree
        Space: O(H) 

        Args:
            root (TreeNode): the root of the tree

        Returns:
            List[int]: all the nodes viewed from the right side
        """

        if not root:
            return []

        output = []

        def dfs(node: TreeNode, lvl: int) -> None:
            if lvl == len(output):
                output.append(node.val)

            for child in [node.right, node.left]:
                if child:
                    dfs(child, lvl+1)
            return
        dfs(root, 0)
        return output

# @lc code=end

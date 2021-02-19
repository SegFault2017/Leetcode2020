#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        Strategy 1: DFS
        Runtime:O(n), where n is the number of nodes
        Space: O(h), where h is the height of the tree
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return "None,"

        output = ""
        output += str(root.val) + ","
        output += self.serialize(root.left)
        output += self.serialize(root.right)
        return output

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        Strategy 1: DFS
        Runtime: O(n)
        Space: O(1)
        :type data: str
        :rtype: TreeNode
        """

        def dfs(node_lst: List[str]) -> TreeNode:
            # if not node_lst:
            #     return None

            if node_lst[0] == "None":
                node_lst.pop(0)
                return None
            root = TreeNode(node_lst[0])
            node_lst.pop(0)
            root.left = dfs(node_lst)
            root.right = dfs(node_lst)
            return root

        return dfs(data.split(","))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

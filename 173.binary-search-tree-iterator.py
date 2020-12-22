#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """Strategy1: In Orider Traversal
    Runtime: O(1), where n is the # of nodes
    Space: O(h)
    """

    # def __init__(self, root: 'TreeNode') -> None:
    #     self.in_order = [-1]
    #     self.inx = 0
    #     self.dfs(root)

    # def dfs(self, node: 'TreeNode') -> None:
    #     if not node:
    #         return

    #     self.dfs(node.left)
    #     self.in_order.append(node.val)
    #     self.dfs(node.right)
    #     return

    # def next(self) -> int:
    #     self.inx += 1
    #     return self.in_order[self.inx]

    # def hasNext(self) -> bool:
    #     return self.inx != len(self.in_order) - 1

    """Strategy1: In Orider Traversal
    Runtime: O(1), where n is the # of nodes
    Space: O(h)
    """

    def leftMost(self, node: 'TreeNode') -> None:
        while node:
            self.stack.append(node)
            node = node.left
        return

    def __init__(self, root: 'TreeNode') -> None:
        self.stack = []
        self.leftMost(root)
        return

    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self.leftMost(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

        # Your BSTIterator object will be instantiated and called as such:
        # obj = BSTIterator(root)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()
        # @lc code=end

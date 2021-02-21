# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """ Strategy : Inorder Traversal
        Runtime:O(n), where n is the number of nodes
        Space: O(n)

        Args:
            root [TreeNode]: the root node
            p [TreeNode]: the target node

        Returns:
            [type]: the sucessor of p
        """

        if not root:
            return None

        stack = []
        cur = root
        inorder = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            inorder.append(cur)
            cur = cur.right

        n = len(inorder)
        for i in range(n+1):
            if i == n-1:
                return None
            if inorder[i].val == p.val:
                return inorder[i+1]
        return None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TreeNode.__repr__ = lambda x: str(x.val)
    def inOrder(self, root: TreeNode, target: int) -> List[int]:
        cache = set()
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            # print(curr.val)
            cache.add(target - curr.val)
            curr = curr.right
        return cache

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        """ Strategy 1: In order + Hash
        Runtime: O(max(n1,n2)), where n1 is the size of root1 and n2 is the size of root2
        Space: O(n1 + n2)

        Args:
            root1 (TreeNode): the root of tree1
            root2 (TreeNode): the root of tree2
            target (int): the target value

        Returns:
            bool: determine wherther there exist 2 nodex,node in tree 1 and a node in tree2, that sums up to target
        """
        order1 = self.inOrder(root1, target)
        # print(order1)
        stack = []

        curr = root2
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val in order1:
                return True
            curr = curr.right
        return False

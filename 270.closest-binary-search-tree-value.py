class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """ Stratefy 1: Binary search
        Runtime: O(log n)
        Space: O(1)

        Args:
            root (TreeNode): the root of the tree
            target (float): the given target value

        Returns:
            int: return the node whose value is closest to the given target value.
        """
        closest = root.val

        while root:
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right

        return closest

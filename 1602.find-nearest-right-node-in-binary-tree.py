class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        """ Strategy 1: BFS with 2 queues
        Runtime: O(n), where n is the number of nodes in the tree
        Space: O(n)

        Args:
            root (TreeNode): the root of the tree
            u (TreeNode): the target node

        Returns:
            TreeNode: return the next node of the target node u
        """
        if root is None:
            return []

        next_level = deque([root, ])
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()

                if node == u:
                    return curr_level.popleft() if curr_level else None
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

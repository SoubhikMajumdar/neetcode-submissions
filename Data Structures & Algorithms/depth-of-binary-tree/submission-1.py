class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        else:
            # Recursively find the depth of the left and right subtrees
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            
            # The depth of the current tree is the maximum of the depths of the left and right subtrees plus 1
            return max(left_depth, right_depth) + 1

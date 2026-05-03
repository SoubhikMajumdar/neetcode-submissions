# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        best = [0]  # stores max diameter (in edges) seen so far

        def height(node):
            if node is None:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            # candidate diameter passing through this node
            best[0] = max(best[0], left_h + right_h)

            # return height of this subtree (in nodes)
            return 1 + max(left_h, right_h)

        height(root)
        return best[0]
        
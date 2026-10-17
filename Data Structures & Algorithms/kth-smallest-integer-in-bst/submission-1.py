# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def kthSmallest(self, root, k):
        count = 0
        result = 0

        def inorder(node):
            nonlocal count, result
            if not node:
                return

            inorder(node.left)
            count+=1

            if count == k:
                result = node.val
                return

            inorder(node.right)

        inorder(root)
        return result
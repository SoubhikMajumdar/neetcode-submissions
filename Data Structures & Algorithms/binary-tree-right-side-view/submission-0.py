class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            # First node we encounter at this depth
            if depth == len(res):
                res.append(node.val)

            # Visit right first so we see the rightmost node first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
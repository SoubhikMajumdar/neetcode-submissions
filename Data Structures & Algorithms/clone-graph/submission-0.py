"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        old_to_new = {}

        def dfs(old_node):
            # Return an existing copy if already cloned
            if old_node in old_to_new:
                return old_to_new[old_node]

            # Create a copy of the current node
            new_node = Node(old_node.val)

            # Save the mapping before exploring neighbors
            old_to_new[old_node] = new_node

            # Clone and connect every neighbor
            for old_neighbor in old_node.neighbors:
                new_neighbor = dfs(old_neighbor)
                new_node.neighbors.append(new_neighbor)

            return new_node

        return dfs(node)
        
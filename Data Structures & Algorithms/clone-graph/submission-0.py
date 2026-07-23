"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_vs_cloned_node = {}
        
        def dfs(node):
            if not node:
                return None
            cloned_node = Node(val = node.val)
            node_vs_cloned_node[node] = cloned_node
            for neighbor in node.neighbors:
                if neighbor not in node_vs_cloned_node:
                    cloned_neighbor = dfs(neighbor)
                    cloned_node.neighbors.append(cloned_neighbor)
                else:
                    cloned_node.neighbors.append(node_vs_cloned_node[neighbor])
            return cloned_node

        return dfs(node)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = inorder_index = 0
        def dfs(limit):
            nonlocal preorder_index, inorder_index
            if preorder_index >= len(preorder):
                return None
            if inorder[inorder_index] == limit:
                inorder_index += 1
                return None
            
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))
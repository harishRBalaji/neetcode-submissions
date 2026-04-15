# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def pre_order_helper(node):
            if not node:
                return
            result.append(node.val)
            pre_order_helper(node.left)
            pre_order_helper(node.right)
        
        pre_order_helper(root)
        return result
        
        
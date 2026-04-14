# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(val, node):
            if node.val <val and not node.right:
                newNode = TreeNode(val)
                node.right = newNode
                return
            elif node.val >= val and not node.left:
                newNode = TreeNode(val)
                node.left = newNode
            elif node.val < val:
                dfs(val, node.right)
            elif node.val >= val:
                dfs(val, node.left)
            else:
                return
        dfs(val, root)
        return root
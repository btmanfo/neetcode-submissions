# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def travelInorder(node):
            if not node:
                return 
            travelInorder(node.left)
            res.append(node.val)
            travelInorder(node.right)
        travelInorder(root)
        return res
                
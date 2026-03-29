# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values = []
        self.inOrderSearch(root)
        return self.values[k-1]

    def inOrderSearch(self, root: TreeNode):
        if root == None:
            return
        
        self.inOrderSearch(root.left)
        self.values.append(root.val)
        self.inOrderSearch(root.right)
    
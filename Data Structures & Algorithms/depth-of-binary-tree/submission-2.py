# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
    
        def dfs(root):
            if root == None:
                return 0
            
            maxSize = 1 + max(dfs(root.left), dfs(root.right))
            self.maxDepth = max(self.maxDepth, maxSize)
            return maxSize
        dfs(root)
        return self.maxDepth
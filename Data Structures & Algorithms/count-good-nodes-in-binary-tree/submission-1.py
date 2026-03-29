# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
        
    def dfs(self, node, maxVal):
        if node == None:
            return 0
        
        if node.val >= maxVal:
            res = 1
        else:
            res = 0
        maxVal = max(maxVal, node.val)
        res = res + self.dfs(node.left, maxVal)
        res = res + self.dfs(node.right, maxVal)
        return res
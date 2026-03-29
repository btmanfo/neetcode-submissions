# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalance = True

        self.dfs(root)

        return self.isBalance

    def dfs(self, head: TreeNode):
        if head == None:
            return 0
        
        right = self.dfs(head.right)
        left = self.dfs(head.left)
        theMax = max(right, left)
        theMin = min(right, left)
        if theMax - theMin >=2:
            self.isBalance = False
        return 1+ theMax
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.rightTree = []
        self.leftTree = []

        self.dsf(p, 1)
        self.dsf(q,2)

        return self.rightTree == self.leftTree

    def dsf(self, head: TreeNode, selectedTable: int):
        if head == None:
            if selectedTable == 1:
                self.rightTree.append(None)
            else:
                self.leftTree.append(None)
            return 0
        
        self.dsf(head.right, selectedTable)
        self.dsf(head.left, selectedTable)

        if selectedTable == 1:
            self.rightTree.append(head.val)
        else:
            self.leftTree.append(head.val)

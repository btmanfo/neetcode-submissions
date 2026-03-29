# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        q1 = deque()
        q1.append(root)
        while q1:
            lol = []
            for i in range(len(q1)):
                tempNode = q1.popleft()
                lol.append(tempNode.val)
                if tempNode.left:
                    q1.append(tempNode.left)
                if tempNode.right:
                    q1.append(tempNode.right)
            res.append(lol)
        return res

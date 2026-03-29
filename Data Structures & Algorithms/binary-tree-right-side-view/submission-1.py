# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            theSize = len(q)
            for i in range(len(q)):
                nodePoped = q.popleft()
                if i == (theSize-1):
                    res.append(nodePoped.val)
                if nodePoped.left:
                    q.append(nodePoped.left)
                if nodePoped.right:
                    q.append(nodePoped.right)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx,val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(l,r):
            if l >r:
                return None
            
            #jai la valeur de mon preorder
            root_val = preorder[self.pre_idx]
            #je change lindex pour ensuite passer a la prochaine valeur de mon preorder
            self.pre_idx +=1

            #je te fait un node de cette valeur
            root = TreeNode(root_val)

            #on trouve lindice de cette valeur
            mid = indices[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0,len(inorder)-1)
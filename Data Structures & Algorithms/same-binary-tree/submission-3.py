# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_deque = deque([p])
        q_deque = deque([q])

        while p_deque and q_deque:
            for _ in range(len(p_deque)):
                node1 = p_deque.popleft()
                node2 = q_deque.popleft()

                if node1 == None and node2 == None:
                    continue
                if node1 == None or node2 == None or node1.val != node2.val:
                    return False
                p_deque.append(node1.left)
                p_deque.append(node1.right)
                q_deque.append(node2.left)
                q_deque.append(node2.right)
        return True
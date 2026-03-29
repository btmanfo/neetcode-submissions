"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        storedNode = {None:None}

        curr = head
        while curr:
            creatNode = Node(curr.val)
            storedNode[curr] = creatNode
            curr = curr.next

        curr = head
        while curr:
            storedNode[curr].next = storedNode[curr.next]
            storedNode[curr].random = storedNode[curr.random]
            curr = curr.next
        return storedNode[head]
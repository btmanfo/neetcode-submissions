# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        firstNode = head
        secondNode = firstNode.next

        while firstNode and secondNode:
            secondNode = secondNode.next
            if secondNode == None:
                return False
            secondNode = secondNode.next
            firstNode = firstNode.next

            if firstNode == secondNode:
                return True
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        headOfNode = dummy
        frontNode = head

        while n>0 and frontNode:
            frontNode = frontNode.next
            n-=1

        while frontNode:
            frontNode = frontNode.next
            headOfNode = headOfNode.next
        headOfNode.next = headOfNode.next.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = ListNode()
        fastPointer = head
        itr = head
        while True:
            if slowPointer == fastPointer:
                return True
            if fastPointer == None:
                return False
            slowPointer = itr
            itr = itr.next

            fastPointer = fastPointer.next
            if fastPointer == None:
                return False
            fastPointer = fastPointer.next
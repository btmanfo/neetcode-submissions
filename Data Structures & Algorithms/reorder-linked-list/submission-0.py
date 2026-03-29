# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        begin = slow
        prev = None
        
        while begin:
            temp = begin.next
            begin.next = prev
            prev = begin
            begin = temp
        
        secondStart = prev
        firstStart = head

        while firstStart and secondStart:
            temp1 = firstStart.next
            temp2 = secondStart.next
            firstStart.next = secondStart
            secondStart.next = temp1
            firstStart = temp1
            secondStart = temp2

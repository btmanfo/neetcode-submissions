# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousLinkedList= None
        currentLinkedList = head

        while currentLinkedList:
            tempLinkedList = currentLinkedList.next
            currentLinkedList.next = previousLinkedList
            previousLinkedList = currentLinkedList
            currentLinkedList = tempLinkedList
        return previousLinkedList
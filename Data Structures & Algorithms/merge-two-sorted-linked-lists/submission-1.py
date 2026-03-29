# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        firstLinked = list1 
        secondLinked = list2
        res = None

        while firstLinked and secondLinked:
            if firstLinked.val <= secondLinked.val:
                res = ListNode(firstLinked.val, res)
                firstLinked = firstLinked.next
            else:
                res = ListNode(secondLinked.val, res)
                secondLinked = secondLinked.next

        while firstLinked:
            res = ListNode(firstLinked.val, res)
            firstLinked = firstLinked.next

        while secondLinked:
            res = ListNode(secondLinked.val, res)
            secondLinked = secondLinked.next

        previous = None
        current = res
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous

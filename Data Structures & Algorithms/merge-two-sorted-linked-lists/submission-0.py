# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        valueTable =[]

        itr = list1

        while itr:
            valueTable.append(itr.val)
            itr = itr.next

        itr2 = list2

        while itr2:
            valueTable.append(itr2.val)
            itr2 = itr2.next
        valueTable.sort(reverse = True)

        myNode= None

        for i in valueTable:
            myNode = ListNode(i, myNode)
        return myNode
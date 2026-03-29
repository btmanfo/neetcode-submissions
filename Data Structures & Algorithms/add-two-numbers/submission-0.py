# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNumber = ''
        secondNumber = ''
        totalNumber = 0

        currl1 = l1
        while currl1:
            firstNumber += str(currl1.val)
            currl1 = currl1.next
        reverseCurrl1 = ''

        for i in range(len(firstNumber)-1,-1,-1):
            reverseCurrl1 += firstNumber[i]

        currl2 = l2
        while currl2:
            secondNumber += str(currl2.val)
            currl2 = currl2.next
        
        reverseCurrl2 = ''

        for i in range(len(secondNumber)-1,-1,-1):
            reverseCurrl2 += secondNumber[i]

        totalNumber = str(int(reverseCurrl1) + int(reverseCurrl2))

        head = None
        for digit in totalNumber:
            createdNode = ListNode(int(digit), head)
            head = createdNode
        return head


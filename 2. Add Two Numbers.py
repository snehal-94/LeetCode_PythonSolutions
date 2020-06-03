You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Solution
________________________________________________

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x=''
        y=''
        while l1:
            x+=str(l1.val)
            l1=l1.next
        while l2:
            y+=str(l2.val)
            l2=l2.next
        z=str(int(x[::-1])+int(y[::-1]))[::-1]
        
        head=dummy=ListNode(0)
        for i in z: 
            head.next=ListNode(int(i))
            head=head.next
        return dummy.next

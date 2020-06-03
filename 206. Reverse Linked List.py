Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Solution 1
__________________________________________________
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack=[]
        dummy=pos=ListNode(0)
        if head is None:
            return None
        if head.next is None:
            return head
        while head:
            if head not in stack:
                stack.append(head.val)
            else:
                break
            head=head.next
        lenS=len(stack)-1
        
        while lenS>=0:
            newNode=ListNode(stack[lenS])
            pos.next=newNode
            pos=pos.next
            lenS-=1
        return dummy.next
        
 Solution 2
 _________________________________________________________
 
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return None
        if head.next is None: return head
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        curr=prev    
        return curr
    
    
  
            
        

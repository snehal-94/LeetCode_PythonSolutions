Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


Solution 1
________________________________________________

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dump=current=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
        current.next=l1 or l2
        return dump.next
        
  Solution 2
  ___________________________________________________
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack=[]
        while l1:
            stack.append(l1.val)
            l1=l1.next
        while l2:
            stack.append(l2.val)
            l2=l2.next
			
        stack=sorted(stack)
        # dummy=ListNode(0)
        if stack:
            s=stack[0]
            head=ListNode(s)
	        
        else:
            head=None
        dummy=head
        for i in range(1,len(stack)):
            s=stack[i]
            newNode=ListNode(s)
            dummy.next=newNode
            dummy=dummy.next
        return head
		
		
		
                
  
  

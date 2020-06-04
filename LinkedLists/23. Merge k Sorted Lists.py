'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


Solution
________________________________________________
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy=head=ListNode(0)
        stack=[]
        for nodes in lists:
            while nodes:
                stack.append(nodes.val)
                nodes=nodes.next
        stack.sort()
        if stack is None:
            return None
        for i in stack:
            head.next=ListNode(i)
            head=head.next
        return dummy.next

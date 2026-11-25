# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        first = dummy

        for i in range(k):
            first = first.next
        
        second = head
        fast = dummy

        for i in range(k):
            fast = fast.next
        
        while fast.next :
            fast = fast.next
            second = second.next
        
        first.val , second.val = second.val , first.val

        return head
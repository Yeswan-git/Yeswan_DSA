# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(head):
            slow = head
            fast = head.next

            while fast and fast.next :
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def merge(lefthead , righthead):
            d = ListNode(0)
            curr = d

            while lefthead and righthead:
                if lefthead.val <= righthead.val:
                    curr.next = lefthead
                    lefthead = lefthead.next
                else:
                    curr.next = righthead
                    righthead = righthead.next
                curr = curr.next
            
            curr.next = lefthead if lefthead else righthead

            return d.next
        
        if head is None or head.next is None :
            return head
        
        mid = middle(head)
        lefthead = head
        righthead = mid.next

        mid.next = None

        lefthead = self.sortList(lefthead)
        righthead = self.sortList(righthead)

        return merge(lefthead , righthead)

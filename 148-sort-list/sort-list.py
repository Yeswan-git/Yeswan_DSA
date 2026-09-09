# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(node):
            slow = node
            fast = node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def merge(leftHead , rightHead):
            d = ListNode(0)
            curr = d
            while leftHead and rightHead :
                if leftHead.val <= rightHead.val:
                    curr.next = leftHead
                    leftHead = leftHead.next
                else:
                    curr.next = rightHead
                    rightHead = rightHead.next
                curr = curr.next
            curr.next = leftHead if leftHead else rightHead
            return d.next

        if not head or not head.next :
            return head
        
        mid = middle(head)
        leaftHead = head
        rightHead = mid.next

        mid.next = None
        
        leftHead = self.sortList(leaftHead)
        rightHead = self.sortList(rightHead)
        return merge(leftHead , rightHead)
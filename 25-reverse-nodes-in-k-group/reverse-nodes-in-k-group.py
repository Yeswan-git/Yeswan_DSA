# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        def get_kth_node(temp , k):
            k -= 1
            while temp and k > 0:
                k -= 1
                temp = temp.next
            return temp

        curr = head
        next_node = None
        prev_node = None

        while curr:
            kth_node = get_kth_node(curr , k)
            if not kth_node:
                if prev_node : prev_node.next = curr
                break
            
            next_node = kth_node.next
            kth_node.next = None
            reverse(curr)
            if curr == head:
                head = kth_node
            else:
                prev_node.next = kth_node
            prev_node = curr
            curr = next_node
        return head
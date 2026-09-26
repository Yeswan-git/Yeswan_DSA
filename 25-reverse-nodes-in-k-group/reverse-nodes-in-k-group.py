# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def reverse(head):
            curr = head
            prev = None
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
        prev_node = None
        next_node = None

        while curr:
            kth_node = get_kth_node(curr , k)
            if kth_node is None:
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
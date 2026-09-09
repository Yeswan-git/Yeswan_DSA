# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None : return head
        n = 1

        tail = head

        while tail.next :
            n += 1
            tail = tail.next
        
        k %= n

        tail.next = head

        for _ in range(n - k):
            tail = tail.next
        
        new_head = tail.next
        tail.next = None

        return new_head
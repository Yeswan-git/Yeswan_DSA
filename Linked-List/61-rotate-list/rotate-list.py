# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head
        tail = head
        n = 1

        while tail.next:
            tail = tail.next
            n += 1
        
        tail.next = head
        k %= n

        for _ in range(n - k):
            tail = tail.next
        
        head = tail.next
        tail.next = None

        return head
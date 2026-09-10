# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)
        res = d

        carry = total = 0

        while l1 or l2 or carry :
            total = carry
            if l1 :
                total += l1.val
                l1 = l1.next
            
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10

            d.next = ListNode(num)
            d = d.next
        
        return res.next